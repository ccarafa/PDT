# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_activitymodel_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymodel',
            name='activity_type',
            field=models.CharField(max_length=128, default='Development'),
        ),
        migrations.AddField(
            model_name='activitymodel',
            name='defects_injected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='activitymodel',
            name='sloc',
            field=models.FloatField(default=0),
        ),
    ]
