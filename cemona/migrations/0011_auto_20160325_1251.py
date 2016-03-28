# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0010_auto_20160325_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkAdapter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('device_id', models.CharField(verbose_name='Device identifier', blank=True, null=True, max_length=16)),
                ('mac', models.CharField(max_length=16)),
                ('type', models.IntegerField(choices=[(1, 'Ethernet'), (2, 'WiFi')], verbose_name='Device type', default=1)),
                ('name', models.CharField(verbose_name='Device name', blank=True, null=True, max_length=100)),
                ('probe', models.ForeignKey(to='cemona.Probe', null=True, verbose_name='Probe', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Network adapters',
                'verbose_name': 'Network adapter',
            },
        ),
        migrations.RemoveField(
            model_name='ethernet',
            name='probe',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='probe',
        ),
        migrations.DeleteModel(
            name='Ethernet',
        ),
        migrations.DeleteModel(
            name='Wifi',
        ),
    ]
