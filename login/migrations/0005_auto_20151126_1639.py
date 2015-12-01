# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151125_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='user_id',
            field=models.IntegerField(unique=True, null=True),
        ),
    ]
