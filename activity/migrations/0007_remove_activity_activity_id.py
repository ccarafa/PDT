# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20151126_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activity_id',
        ),
    ]
