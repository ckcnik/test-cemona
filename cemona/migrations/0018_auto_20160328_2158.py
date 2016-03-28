# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0017_auto_20160328_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modem',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', related_name='modems', verbose_name='Probe', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='networkadapter',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', related_name='net_adapters', verbose_name='Probe', null=True, blank=True),
        ),
    ]
