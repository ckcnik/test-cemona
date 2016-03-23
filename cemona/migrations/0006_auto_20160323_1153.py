# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0005_auto_20160323_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='RegisterAction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('numstatemodem', models.IntegerField()),
                ('idactionvalue', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name='Date created', default=django.utils.timezone.now)),
                ('beggroup', models.IntegerField()),
                ('curgroup', models.IntegerField(null=True, blank=True)),
                ('endgroup', models.IntegerField(null=True, blank=True)),
                ('closed', models.DateTimeField(null=True, blank=True)),
                ('action', models.ForeignKey(to='cemona.Event', unique=True)),
                ('modem', models.ForeignKey(to='cemona.Modem', verbose_name='Modem')),
            ],
            options={
                'verbose_name': 'Event registration',
                'verbose_name_plural': 'Events registration',
            },
        ),
        migrations.AlterUniqueTogether(
            name='registeraction',
            unique_together=set([('modem', 'numstatemodem', 'action', 'idactionvalue')]),
        ),
    ]
