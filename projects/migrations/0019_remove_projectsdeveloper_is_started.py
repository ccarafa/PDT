# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20151130_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectsdeveloper',
            name='is_started',
        ),
    ]
