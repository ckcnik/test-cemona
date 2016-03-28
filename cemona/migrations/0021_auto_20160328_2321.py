# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0020_auto_20160328_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='modem',
            name='fw',
            field=models.CharField(null=True, max_length=10, blank=True, verbose_name='FW modem'),
        ),
        migrations.AddField(
            model_name='modem',
            name='hw',
            field=models.CharField(null=True, max_length=10, blank=True, verbose_name='HW modem'),
        ),
        migrations.AddField(
            model_name='modem',
            name='imei',
            field=models.BigIntegerField(default=0, verbose_name='Modem IMEI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modem',
            name='imsi',
            field=models.CharField(null=True, max_length=20, blank=True, verbose_name='Modem IMSI'),
        ),
        migrations.AddField(
            model_name='modem',
            name='manufacturer',
            field=models.CharField(null=True, max_length=50, blank=True, verbose_name='Modem manufacturer'),
        ),
        migrations.AddField(
            model_name='modem',
            name='model',
            field=models.CharField(null=True, max_length=50, blank=True, verbose_name='Modem model'),
        ),
        migrations.AddField(
            model_name='modem',
            name='probe',
            field=models.ForeignKey(blank=True, verbose_name='Probe', to='cemona.Probe', null=True, related_name='modems'),
        ),
        migrations.AlterField(
            model_name='modem',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True),
        ),
    ]
