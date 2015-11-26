# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phases',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField()),
                ('hours', models.IntegerField()),
                ('defects', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
