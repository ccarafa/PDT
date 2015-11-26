# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_auto_20151126_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='defects_injected',
            new_name='defects',
        ),
        migrations.AddField(
            model_name='activity',
            name='username',
            field=models.CharField(max_length=128, default='unnamed user'),
        ),
    ]
