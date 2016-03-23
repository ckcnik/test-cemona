# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemona', '0006_auto_20160323_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeraction',
            name='action',
            field=models.ForeignKey(to='cemona.Event'),
        ),
    ]
