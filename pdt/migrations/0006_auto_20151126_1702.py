# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0005_auto_20151126_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='manageriteration',
            name='est_sloc',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AddField(
            model_name='managerphase',
            name='est_sloc',
            field=models.IntegerField(null=True, default=0),
        ),
    ]
