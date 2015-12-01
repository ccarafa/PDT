# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20151126_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managerproject',
            old_name='uid',
            new_name='project_id',
        ),
    ]
