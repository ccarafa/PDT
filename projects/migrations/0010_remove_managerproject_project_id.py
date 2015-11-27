# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_managerproject_estimate_sloc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerproject',
            name='project_id',
        ),
    ]
