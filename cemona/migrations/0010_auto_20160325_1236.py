# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0009_auto_20160325_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ethernet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('device_id', models.CharField(null=True, max_length=16, blank=True, verbose_name='Identifier device')),
                ('mac', models.CharField(max_length=16)),
                ('probe', models.ForeignKey(null=True, to='cemona.Probe', verbose_name='Probe', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Ethernet',
                'verbose_name': 'Ethernet',
            },
        ),
        migrations.CreateModel(
            name='Wifi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('device_id', models.CharField(null=True, max_length=16, blank=True, verbose_name='Identifier device')),
                ('mac', models.CharField(max_length=16)),
                ('probe', models.ForeignKey(null=True, to='cemona.Probe', verbose_name='Probe', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Ethernet',
                'verbose_name': 'Ethernet',
            },
        ),
        migrations.RenameField(
            model_name='modem',
            old_name='name',
            new_name='device_id',
        ),
    ]
