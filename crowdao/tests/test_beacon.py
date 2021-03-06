from unittest import mock

from django.core.urlresolvers import reverse
from .common import BaseTestCase
from ..models.order import Order, ORDER_STATUS_FINAL, ORDER_STATUS_REIMBURSED, \
    ORDER_STATUS_TRANSFERRED
from ..models.campaign import CAMPAIGN_STATUS_FAILED, Campaign
from .common import mock_stripe


class BeaconCampaignTests(BaseTestCase):

    @mock_stripe
    def test_beacon_campaign_lifecycle(self):
        # create a Beacon Campaign
        bc = Campaign(
            name='Test Campaign',
            goal=100,
            ctype='BEACON',
            )

        bc.save()
        # collect a donation 1
        order1 = Order(
            amount=10,
            notify=False,
            campaign=bc,
            )

        order1.pledge()
        order1.save()

        self.assertEqual(bc.orders.count(), 1)
        self.assertEqual(bc.total_pledged(), 10)

        # collect a recurrent donation 2
        # collect a donation 1
        order2 = Order(
            amount=20,
            notify=False,
            campaign=bc,
            recurrent=True,
            )

        order2.pledge()
        order2.save()

        self.assertEqual(bc.orders.count(), 2)
        self.assertEqual(bc.total_pledged(), 30)

        # the first period of the campaign ends, but the goal is not reached
        self.assertEqual(bc.goal_reached(), False)
        bc.close_campaign()

        self.assertEqual(bc.status, CAMPAIGN_STATUS_FAILED)
        next_campaign = bc.next_campaign

        # donation 1 and 2 are now cancelled
        order1.refresh_from_db()
        order2.refresh_from_db()
        self.assertEqual(order1.status, ORDER_STATUS_REIMBURSED)
        self.assertEqual(order2.status, ORDER_STATUS_TRANSFERRED)

        # but the payment of order2 is now transferred to the new campaign
        self.assertEqual(next_campaign.orders.count(), 1)
        self.assertEqual(next_campaign.total_pledged(), 20)

        # add another donation, to reach the goal
        order4 = Order(
            amount=100,
            notify=False,
            campaign=next_campaign,
            recurrent=True,
            )

        order4.save()

        # now the goal is reached
        self.assertEqual(next_campaign.goal_reached(), True)
        next_campaign.close_campaign()

        # and the end period, the campaign funds are collected
        self.assertEqual(next_campaign.orders.count(), 2)
        for order in next_campaign.orders.all():  
            self.assertEqual(order.status, ORDER_STATUS_FINAL)


