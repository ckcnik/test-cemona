# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('manufacturer', models.CharField(max_length=50, blank=True, null=True)),
                ('model', models.CharField(max_length=50, blank=True, null=True)),
                ('imei', models.CharField(max_length=16, blank=True, null=True)),
                ('hw', models.CharField(max_length=10, blank=True, null=True)),
                ('fw', models.CharField(max_length=10, blank=True, null=True)),
                ('imsi_sim', models.CharField(max_length=20, blank=True, null=True)),
                ('time_zone', models.CharField(max_length=20, blank=True, null=True)),
                ('apn', models.CharField(max_length=20, blank=True, null=True)),
                ('apn_user', models.CharField(max_length=20, blank=True, null=True)),
                ('apn_password', models.CharField(max_length=20, blank=True, null=True)),
                ('ras', models.IntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('test_status', models.TextField(blank=True, null=True)),
                ('mode', models.TextField(blank=True, null=True)),
                ('ethernet_test_status', models.TextField(blank=True, null=True)),
                ('wifi_test_status', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Modem',
                'verbose_name_plural': 'Modems',
            },
        ),
    ]
