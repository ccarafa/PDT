# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20151202_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='defect',
            name='defect_id',
            field=models.IntegerField(default=0),
        ),
    ]
