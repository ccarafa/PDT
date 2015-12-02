# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_remove_project_defects'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteration',
            name='twentypercent',
            field=models.FloatField(default=0.0),
        ),
    ]
