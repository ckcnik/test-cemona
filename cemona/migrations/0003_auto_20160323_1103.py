# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0002_auto_20160323_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('codeid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Measurements',
                'verbose_name': 'Measurement',
            },
        ),
        migrations.AlterField(
            model_name='modem',
            name='apn',
            field=models.CharField(blank=True, null=True, verbose_name='Modem APN', max_length=20),
        ),
        migrations.AlterField(
            model_name='modem',
            name='apn_password',
            field=models.CharField(blank=True, null=True, verbose_name='Modem APN password', max_length=20),
        ),
        migrations.AlterField(
            model_name='modem',
            name='apn_user',
            field=models.CharField(blank=True, null=True, verbose_name='Modem APN user', max_length=20),
        ),
        migrations.AlterField(
            model_name='modem',
            name='fw',
            field=models.CharField(blank=True, null=True, verbose_name='FW modem', max_length=10),
        ),
        migrations.AlterField(
            model_name='modem',
            name='hw',
            field=models.CharField(blank=True, null=True, verbose_name='HW modem', max_length=10),
        ),
        migrations.AlterField(
            model_name='modem',
            name='imei',
            field=models.CharField(blank=True, null=True, verbose_name='Modem IMEI', max_length=16),
        ),
        migrations.AlterField(
            model_name='modem',
            name='imsi_sim',
            field=models.CharField(blank=True, null=True, verbose_name='Modem IMSI', max_length=20),
        ),
        migrations.AlterField(
            model_name='modem',
            name='manufacturer',
            field=models.CharField(blank=True, null=True, verbose_name='Modem manufacturer', max_length=50),
        ),
        migrations.AlterField(
            model_name='modem',
            name='model',
            field=models.CharField(blank=True, null=True, verbose_name='Modem model', max_length=50),
        ),
        migrations.AlterField(
            model_name='modem',
            name='ras',
            field=models.IntegerField(blank=True, null=True, verbose_name='Modem RAS number'),
        ),
        migrations.AlterField(
            model_name='modem',
            name='time_zone',
            field=models.CharField(blank=True, null=True, verbose_name='Time Zone', max_length=20),
        ),
    ]
