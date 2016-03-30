# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='LoggingModem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Date created', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Logging Modem',
                'verbose_name_plural': 'Logging Modems',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('codeid', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Measurement',
                'verbose_name_plural': 'Measurements',
            },
        ),
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.BigIntegerField(verbose_name='Modem IMEI')),
                ('manufacturer', models.CharField(max_length=50, blank=True, verbose_name='Modem manufacturer', null=True)),
                ('model', models.CharField(max_length=50, blank=True, verbose_name='Modem model', null=True)),
                ('hw', models.CharField(max_length=10, blank=True, verbose_name='HW modem', null=True)),
                ('fw', models.CharField(max_length=10, blank=True, verbose_name='FW modem', null=True)),
                ('imsi', models.CharField(max_length=20, blank=True, verbose_name='Modem IMSI', null=True)),
            ],
            options={
                'verbose_name': 'Modem',
                'verbose_name_plural': 'Modems',
            },
        ),
        migrations.CreateModel(
            name='NetworkAdapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=16, blank=True, verbose_name='Device identifier', null=True)),
                ('mac', models.CharField(max_length=20)),
                ('type', models.IntegerField(choices=[(1, 'Ethernet'), (2, 'WiFi')], default=1, verbose_name='Device type')),
                ('name', models.CharField(max_length=100, blank=True, verbose_name='Device name', null=True)),
            ],
            options={
                'verbose_name': 'Network adapter',
                'verbose_name_plural': 'Network adapters',
            },
        ),
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(unique=True, max_length=50, verbose_name='Serial number')),
                ('ram_size', models.IntegerField(verbose_name='Memory Size')),
                ('sd_size', models.IntegerField()),
                ('os_version', models.CharField(max_length=100)),
                ('csw_version', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Probe',
                'verbose_name_plural': 'Probes',
            },
        ),
        migrations.CreateModel(
            name='RegisterAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numstatemodem', models.IntegerField()),
                ('idactionvalue', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name='Date created', default=django.utils.timezone.now)),
                ('beggroup', models.IntegerField()),
                ('curgroup', models.IntegerField(null=True, blank=True)),
                ('endgroup', models.IntegerField(null=True, blank=True)),
                ('closed', models.DateTimeField(null=True, blank=True)),
                ('action', models.ForeignKey(to='cemona.Event')),
                ('modem', models.ForeignKey(to='cemona.Modem', verbose_name='Modem')),
            ],
            options={
                'verbose_name': 'Event registration',
                'verbose_name_plural': 'Events registration',
            },
        ),
        migrations.CreateModel(
            name='RegisterMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcodemeasurment', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name='Date created', default=django.utils.timezone.now)),
                ('measurement', models.ForeignKey(to='cemona.Measurement', verbose_name='Measurement')),
            ],
            options={
                'verbose_name': 'Modem',
                'verbose_name_plural': 'Modems',
            },
        ),
        migrations.AddField(
            model_name='networkadapter',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', blank=True, related_name='net_adapters', verbose_name='Probe', null=True),
        ),
        migrations.AddField(
            model_name='modem',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', blank=True, related_name='modems', verbose_name='Probe', null=True),
        ),
        migrations.AddField(
            model_name='loggingmodem',
            name='modem',
            field=models.ForeignKey(to='cemona.Modem', verbose_name='Modem APN'),
        ),
        migrations.AddField(
            model_name='loggingmodem',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', verbose_name='Modem APN'),
        ),
        migrations.AlterUniqueTogether(
            name='registeraction',
            unique_together=set([('modem', 'numstatemodem', 'action', 'idactionvalue')]),
        ),
    ]
