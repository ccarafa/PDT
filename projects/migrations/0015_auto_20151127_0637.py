# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20151127_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteration',
            name='estimate_sloc',
        ),
        migrations.RemoveField(
            model_name='iteration',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='iteration',
            name='sloc',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='estimate_sloc',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='sloc',
        ),
    ]
