# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0014_auto_20160325_1724'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='modem',
            unique_together=set([('probe', 'device_id')]),
        ),
    ]
