# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20151126_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='user_id',
        ),
    ]
