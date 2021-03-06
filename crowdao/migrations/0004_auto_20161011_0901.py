# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-11 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdao', '0003_order_charge_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BeaconCampaign',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='ctype',
            field=models.CharField(choices=[('BEACON', 'BEACON')], max_length=6, verbose_name='Campagin Type'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='duration',
            field=models.IntegerField(default='7', verbose_name='Duration of the campaign'),
        ),
        # # migrations.AlterField(
        # #     model_name='campaign',
        # #     name='goal',
        # #     field=models.DecimalField(decimal_places=2, default=500, max_digits=8, verbose_name='Goal'),
        # ),
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Campaign Name'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[('FAILED', 'FAILED'), ('ACTIVE', 'ACTIVE')], default='ACTIVE', max_length=6, verbose_name='Campaign status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='addr1',
            field=models.CharField(default='', max_length=255, verbose_name='Address 1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='addr2',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Address 2'),
        ),
        # migrations.AlterField(
        #     model_name='order',
        #     name='amount',
        #     field=models.DecimalField(decimal_places=2, default='', max_digits=8, verbose_name='Amount'),
        # ),
        migrations.AlterField(
            model_name='order',
            name='charge_id',
            field=models.CharField(max_length=255, null=True, verbose_name='Stripe Charge id'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=255, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='', max_length=255, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='namecredit',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Credit Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='order',
            name='notify',
            field=models.BooleanField(verbose_name='Notify me if the project team posts an update?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pcode',
            field=models.CharField(default='', max_length=255, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pref',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Payment Reference'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ptype',
            field=models.CharField(choices=[('CC', 'Credit Card'), ('BC', 'Bitcoin'), ('PP', 'PayPal'), ('BT', 'Bank Transfer')], max_length=2, verbose_name='Payment Type'),
        ),
        migrations.AlterField(
            model_name='order',
            name='recurrent',
            field=models.BooleanField(default=False, verbose_name='Make this a recurrent donation'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='crowdao.Reward', verbose_name='Reward Level'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=255, verbose_name='State/Province'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('REIMBU', 'REIMBURSED'), ('FINAL', 'FINALIZED'), ('TRANSF', 'Transferred to follow-up campaign')], max_length=10, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='question',
            name='notify',
            field=models.BooleanField(default=True, verbose_name='Notify me on replies'),
        ),
        migrations.AlterField(
            model_name='question',
            name='orig',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='crowdao.Question', verbose_name='In reply to'),
        ),
        migrations.AlterField(
            model_name='question',
            name='team_response',
            field=models.BooleanField(default=False, verbose_name='Add the Team Response flag'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='desc',
            field=models.CharField(default='', max_length=255, verbose_name='Reward Description'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='fine_print',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Fine Print'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='icon_class',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Icon Classes'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='img',
            field=models.URLField(blank=True, default='', verbose_name='Image URL'),
        ),
        # migrations.AlterField(
        #     model_name='reward',
        #     name='min_amount',
        #     field=models.DecimalField(decimal_places=2, default='', max_digits=8, verbose_name='Minimum Amount'),
        # ),
        migrations.AlterField(
            model_name='reward',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Reward Name'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='short_desc',
            field=models.CharField(default='', max_length=255, verbose_name='Short Reward Description'),
        ),
        migrations.AlterField(
            model_name='update',
            name='author',
            field=models.CharField(max_length=255, verbose_name='Author Name'),
        ),
        migrations.AlterField(
            model_name='update',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Author Email'),
        ),
        migrations.AlterField(
            model_name='value',
            name='type',
            field=models.CharField(max_length=7, verbose_name='Currency Abbreviation'),
        ),
        migrations.AlterField(
            model_name='value',
            name='update',
            field=models.BooleanField(verbose_name='Update value from API?'),
        ),
        migrations.AlterField(
            model_name='value',
            name='value',
            field=models.FloatField(verbose_name='USD to currency'),
        ),
    ]
