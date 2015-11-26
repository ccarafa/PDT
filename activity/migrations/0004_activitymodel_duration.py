# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_activitymodel_pause_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymodel',
            name='duration',
            field=models.CharField(max_length=120, default=0),
        ),
    ]
