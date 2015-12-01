# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20151126_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=75, default='unnamed project')),
                ('phase_name', models.CharField(max_length=75, default='unnamed phase')),
                ('iteration_name', models.CharField(max_length=25, default='unnamed iteration')),
                ('activity_type', models.CharField(max_length=128, default='Development')),
                ('username', models.CharField(max_length=128, default='unnamed user')),
                ('start_time', models.CharField(max_length=120, default=0)),
                ('pause_time', models.CharField(max_length=120, default=0)),
                ('duration', models.CharField(max_length=120, default=0)),
                ('sloc', models.FloatField(default=0)),
                ('defects', models.IntegerField(default=0)),
                ('is_open', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='iteration',
            name='iteration_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='iteration',
            name='phase_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='iteration',
            name='project_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='phase_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='project_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='projectsdeveloper',
            name='developer_name',
            field=models.CharField(max_length=120, default='-'),
        ),
        migrations.AlterField(
            model_name='projectsdeveloper',
            name='project_name',
            field=models.CharField(max_length=120, default='-'),
        ),
    ]
