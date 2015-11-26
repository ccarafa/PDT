# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_activity_is_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='iteration_id',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='phase_id',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='user_id',
        ),
        migrations.AddField(
            model_name='activity',
            name='iteration_name',
            field=models.CharField(max_length=25, default='unnamed iteration'),
        ),
        migrations.AddField(
            model_name='activity',
            name='phase_name',
            field=models.CharField(max_length=75, default='unnamed phase'),
        ),
        migrations.AddField(
            model_name='activity',
            name='project_name',
            field=models.CharField(max_length=75, default='unnamed project'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(max_length=128, default='development'),
        ),
    ]
