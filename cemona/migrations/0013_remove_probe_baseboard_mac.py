# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0012_auto_20160325_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probe',
            name='baseboard_mac',
        ),
    ]
