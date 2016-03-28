# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0011_auto_20160325_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='modem',
            name='fw',
            field=models.CharField(verbose_name='FW modem', blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='probe',
            name='baseboard_mac',
            field=models.CharField(max_length=20),
        ),
    ]
