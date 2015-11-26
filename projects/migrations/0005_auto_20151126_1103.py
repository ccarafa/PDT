# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20151126_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerproject',
            name='developers',
        ),
        migrations.AddField(
            model_name='managerproject',
            name='manager',
            field=models.CharField(default=b'-', max_length=120),
        ),
    ]
