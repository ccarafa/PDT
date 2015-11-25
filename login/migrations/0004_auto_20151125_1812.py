# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20151125_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='role',
            field=models.CharField(max_length=80),
        ),
    ]
