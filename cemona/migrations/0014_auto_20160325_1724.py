# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0013_remove_probe_baseboard_mac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkadapter',
            name='mac',
            field=models.CharField(max_length=20),
        ),
    ]
