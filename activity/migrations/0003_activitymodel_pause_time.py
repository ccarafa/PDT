# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_activitymodel_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymodel',
            name='pause_time',
            field=models.CharField(max_length=120, default=0),
        ),
    ]
