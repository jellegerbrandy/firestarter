# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-03 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeaconCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name=b'Name')),
                ('addr1', models.CharField(default=b'', max_length=255, verbose_name=b'Address 1')),
                ('addr2', models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Address 2')),
                ('city', models.CharField(default=b'', max_length=255, verbose_name=b'City')),
                ('state', models.CharField(default=b'', max_length=255, verbose_name=b'State/Province')),
                ('pcode', models.CharField(default=b'', max_length=255, verbose_name=b'Postal Code')),
                ('country', models.CharField(default=b'', max_length=255, verbose_name=b'Country')),
                ('amount', models.DecimalField(decimal_places=2, default=b'', max_digits=8, verbose_name=b'Amount')),
                ('ptype', models.CharField(choices=[(b'CC', b'Credit Card'), (b'BC', b'Bitcoin'), (b'PP', b'PayPal'), (b'BT', b'Bank Transfer')], max_length=2, verbose_name=b'Payment Type')),
                ('pref', models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Payment Reference')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('notify', models.BooleanField(verbose_name=b'Notify me if the project team posts an update?')),
                ('namecredit', models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Credit Name')),
                ('notes', models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name=b'Email')),
                ('text', models.TextField()),
                ('notify', models.BooleanField(default=True, verbose_name=b'Notify me on replies')),
                ('team_response', models.BooleanField(default=False, verbose_name=b'Add the Team Response flag')),
                ('orig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='crowdao.Question', verbose_name=b'In reply to')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=255, verbose_name=b'Reward Name')),
                ('min_amount', models.DecimalField(decimal_places=2, default=b'', max_digits=8, verbose_name=b'Minimum Amount')),
                ('desc', models.CharField(default=b'', max_length=255, verbose_name=b'Reward Description')),
                ('short_desc', models.CharField(default=b'', max_length=255, verbose_name=b'Short Reward Description')),
                ('fine_print', models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Fine Print')),
                ('icon_class', models.CharField(blank=True, default=b'', max_length=255, verbose_name=b'Icon Classes')),
                ('img', models.URLField(blank=True, default=b'', verbose_name=b'Image URL')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255, verbose_name=b'Author Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Author Email')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=7, verbose_name=b'Currency Abbreviation')),
                ('value', models.FloatField(verbose_name=b'USD to currency')),
                ('update', models.BooleanField(verbose_name=b'Update value from API?')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='reward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='crowdao.Reward', verbose_name=b'Reward Level'),
        ),
    ]