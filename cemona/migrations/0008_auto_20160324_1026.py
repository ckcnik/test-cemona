# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0007_auto_20160323_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggingModem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
            ],
            options={
                'verbose_name_plural': 'Logging Modems',
                'verbose_name': 'Logging Modem',
            },
        ),
        migrations.AlterField(
            model_name='modem',
            name='probe',
            field=models.ForeignKey(null=True, verbose_name='Probe', blank=True, to='cemona.Probe'),
        ),
        migrations.AddField(
            model_name='loggingmodem',
            name='modem',
            field=models.ForeignKey(to='cemona.Modem', verbose_name='Modem APN'),
        ),
        migrations.AddField(
            model_name='loggingmodem',
            name='probe',
            field=models.ForeignKey(to='cemona.Probe', verbose_name='Modem APN'),
        ),
    ]
