# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20151126_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsDeveloper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(default=b'-', max_length=120)),
                ('developer_name', models.CharField(default=b'-', max_length=120)),
            ],
        ),
    ]
