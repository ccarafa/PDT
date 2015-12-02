# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_remove_managerproject_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerproject',
            name='defects',
            field=models.IntegerField(default=0),
        ),
    ]
