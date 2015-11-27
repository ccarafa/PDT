# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=120)),
                ('inception_phase', models.IntegerField()),
                ('elaboration_phase', models.IntegerField()),
                ('construction_phase', models.IntegerField()),
                ('transition_phase', models.IntegerField()),
                ('inception_iteration_1', models.IntegerField()),
                ('eleboration_iteration_1', models.IntegerField()),
                ('eleboration_iteration_2', models.IntegerField()),
                ('construction_iteration_1', models.IntegerField()),
                ('construction_iteration_2', models.IntegerField()),
                ('construction_iteration_3', models.IntegerField()),
                ('transition_iteration_1', models.IntegerField()),
                ('transition_iteration_2', models.IntegerField()),
                ('developers', models.IntegerField()),
                ('is_open', models.BooleanField()),
            ],
        ),
    ]
