# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('role', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]
