# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_remove_activity_activity_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
    ]
