# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(unique=True, max_length=50)),
                ('memory_size', models.IntegerField()),
                ('sd_size', models.IntegerField()),
                ('mac_address', models.CharField(max_length=16)),
                ('os_version', models.CharField(max_length=100)),
                ('control_sw_version', models.CharField(max_length=100)),
                ('communication_device', models.CharField(blank=True, max_length=20, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('ip_mask', models.GenericIPAddressField(blank=True, null=True)),
                ('ip_gateway', models.GenericIPAddressField(blank=True, null=True)),
                ('dns', models.GenericIPAddressField(blank=True, null=True)),
                ('ftp_address', models.GenericIPAddressField(blank=True, null=True)),
                ('ftp_login', models.CharField(blank=True, max_length=20, null=True)),
                ('ftp_password', models.CharField(blank=True, max_length=20, null=True)),
                ('ftp_port', models.IntegerField(blank=True, null=True)),
                ('ftp_period', models.IntegerField(blank=True, null=True)),
                ('http_address', models.GenericIPAddressField(blank=True, null=True)),
                ('http_port', models.IntegerField(blank=True, null=True)),
                ('http_period', models.IntegerField(blank=True, null=True)),
                ('critical_sd_size', models.IntegerField(blank=True, null=True)),
                ('ssid', models.CharField(blank=True, max_length=10, null=True)),
                ('wifi_security', models.TextField(blank=True, null=True)),
                ('wifi_encription', models.TextField(blank=True, null=True)),
                ('wifi_password', models.CharField(blank=True, max_length=20, null=True)),
                ('wifi_state', models.TextField(blank=True, null=True)),
                ('ethernet_test_status', models.CharField(blank=True, max_length=10, null=True)),
                ('wifi_test_status', models.CharField(blank=True, max_length=10, null=True)),
                ('gps_status', models.TextField(blank=True, null=True)),
                ('ethernet_status', models.TextField(blank=True, null=True)),
                ('wifi_status', models.TextField(blank=True, null=True)),
                ('probe_status', models.TextField(blank=True, null=True)),
                ('work_mode', models.TextField(blank=True, null=True)),
                ('target_type', models.TextField(blank=True, null=True)),
                ('position_system', models.TextField(blank=True, null=True)),
                ('ftp_mode', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Probe',
                'verbose_name_plural': 'Probes',
            },
        ),
        migrations.AddField(
            model_name='modem',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', verbose_name='Probe'),
            preserve_default=False,
        ),
    ]
