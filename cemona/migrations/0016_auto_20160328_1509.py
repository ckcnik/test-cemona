# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0015_auto_20160325_1829'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='modem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='modem',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='modem',
            name='imei',
        ),
    ]
