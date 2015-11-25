# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20151124_2218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Signin',
        ),
    ]
