# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0016_auto_20160328_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modem',
            name='id',
        ),
        migrations.AddField(
            model_name='modem',
            name='imei',
            field=models.BigIntegerField(primary_key=True, verbose_name='Modem IMEI', default=0, serialize=False),
            preserve_default=False,
        ),
    ]
