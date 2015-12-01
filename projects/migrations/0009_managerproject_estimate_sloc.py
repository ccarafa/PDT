# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_projectsdeveloper'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerproject',
            name='estimate_sloc',
            field=models.IntegerField(default=0),
        ),
    ]
