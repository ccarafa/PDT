# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_managerproject_defects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0)),
                ('est_sloc', models.IntegerField(default=0)),
                ('hours', models.IntegerField(default=0)),
                ('iteration_name', models.CharField(default=b'-', max_length=120)),
                ('phase_name', models.CharField(default=b'-', max_length=120)),
                ('project_name', models.CharField(default=b'-', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0)),
                ('est_sloc', models.IntegerField(default=0)),
                ('hours', models.IntegerField(default=0)),
                ('phase_name', models.CharField(default=b'-', max_length=120)),
                ('project_name', models.CharField(default=b'-', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(default=b'-', max_length=120)),
                ('is_open', models.BooleanField(default=False)),
                ('estimate_sloc', models.IntegerField(default=0)),
                ('sloc', models.IntegerField(default=0)),
                ('hours', models.IntegerField(default=0)),
                ('manager', models.CharField(default=b'-', max_length=120)),
                ('defects', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='ManagerProject',
        ),
    ]
