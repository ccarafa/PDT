# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151126_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperIteration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0, null=True)),
                ('hours', models.IntegerField(default=0, null=True)),
                ('defects', models.IntegerField(default=0, null=True)),
                ('iteration_name', models.CharField(default=b'-', max_length=25, null=True)),
                ('phase_name', models.CharField(default=b'-', max_length=75)),
                ('project_name', models.CharField(default=b'-', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperPhase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(null=True)),
                ('hours', models.IntegerField(null=True)),
                ('defects', models.IntegerField(null=True)),
                ('phase_name', models.CharField(default=b'-', max_length=25, null=True)),
                ('project_name', models.CharField(default=b'-', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerIteration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0, null=True)),
                ('est_sloc', models.IntegerField(default=0, null=True)),
                ('hours', models.IntegerField(default=0, null=True)),
                ('defects', models.IntegerField(default=0, null=True)),
                ('iteration_name', models.CharField(default=b'-', max_length=25, null=True)),
                ('phase_name', models.CharField(default=b'-', max_length=75)),
                ('project_name', models.CharField(default=b'-', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerPhase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0, null=True)),
                ('est_sloc', models.IntegerField(default=0, null=True)),
                ('hours', models.IntegerField(default=0, null=True)),
                ('defects', models.IntegerField(default=0, null=True)),
                ('phase_name', models.CharField(default=b'-', max_length=25, null=True)),
                ('project_name', models.CharField(default=b'-', max_length=75)),
            ],
        ),
    ]
