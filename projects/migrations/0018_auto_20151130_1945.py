# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20151130_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteration',
            name='phase_name',
            field=models.CharField(default=b'-', max_length=200),
        ),
    ]
