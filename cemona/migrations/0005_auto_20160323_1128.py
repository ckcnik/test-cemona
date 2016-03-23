# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0004_registermeasurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermeasurement',
            name='created',
            field=models.DateTimeField(verbose_name='Date created', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registermeasurement',
            name='measurement',
            field=models.ForeignKey(verbose_name='Measurement', to='cemona.Measurement'),
        ),
    ]
