# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0003_auto_20151125_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(null=True)),
                ('hours', models.IntegerField(null=True)),
                ('defects', models.IntegerField(null=True)),
                ('name', models.CharField(null=True, max_length=25)),
                ('phasename', models.CharField(default='unnamed phase', max_length=75)),
                ('projectname', models.CharField(default='unnamed project', max_length=75)),
            ],
        ),
        migrations.RenameModel(
            old_name='Phases',
            new_name='Phase',
        ),
    ]
