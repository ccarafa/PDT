# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151126_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerproject',
            name='hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='managerproject',
            name='sloc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='managerproject',
            name='uid',
            field=models.IntegerField(default=0),
        ),
    ]
