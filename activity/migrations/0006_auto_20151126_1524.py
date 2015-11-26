# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_auto_20151126_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('project_id', models.IntegerField(default=0)),
                ('phase_id', models.IntegerField(default=0)),
                ('iteration_id', models.IntegerField(default=0)),
                ('activity_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('start_time', models.CharField(max_length=120, default=0)),
                ('pause_time', models.CharField(max_length=120, default=0)),
                ('duration', models.CharField(max_length=120, default=0)),
                ('sloc', models.FloatField(default=0)),
                ('activity_type', models.CharField(max_length=128, default='Development')),
                ('defects_injected', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='ActivityModel',
        ),
    ]
