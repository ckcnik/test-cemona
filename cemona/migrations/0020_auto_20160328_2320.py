# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0019_auto_20160328_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modem',
            name='fw',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='hw',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='imei',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='imsi',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='model',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='probe',
        ),
    ]
