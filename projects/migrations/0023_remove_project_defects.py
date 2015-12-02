# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_defect_defect_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='defects',
        ),
    ]
