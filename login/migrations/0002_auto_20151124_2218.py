# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
