# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0003_auto_20160323_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterMeasurement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('idcodemeasurment', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('measurement', models.ForeignKey(to='cemona.Measurement')),
            ],
            options={
                'verbose_name_plural': 'Modems',
                'verbose_name': 'Modem',
            },
        ),
    ]
