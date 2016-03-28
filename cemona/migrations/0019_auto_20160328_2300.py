# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0018_auto_20160328_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modem',
            name='imei',
            field=models.BigIntegerField(verbose_name='Modem IMEI'),
        ),
        migrations.AddField(
            model_name='modem',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True),
            preserve_default=False,
        ),
    ]
