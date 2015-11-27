# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20151126_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iteration',
            old_name='est_sloc',
            new_name='estimate_sloc',
        ),
        migrations.RenameField(
            model_name='phase',
            old_name='est_sloc',
            new_name='estimate_sloc',
        ),
    ]
