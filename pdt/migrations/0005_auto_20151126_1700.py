# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0004_auto_20151125_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperIteration',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0, null=True)),
                ('hours', models.IntegerField(default=0, null=True)),
                ('defects', models.IntegerField(default=0, null=True)),
                ('iteration_name', models.CharField(default='unnamed iteration', max_length=25, null=True)),
                ('phase_name', models.CharField(default='unnamed phase', max_length=75)),
                ('project_name', models.CharField(default='unnamed project', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperPhase',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(null=True)),
                ('hours', models.IntegerField(null=True)),
                ('defects', models.IntegerField(null=True)),
                ('phase_name', models.CharField(default='unnamed phase', max_length=25, null=True)),
                ('project_name', models.CharField(default='unnamed project', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerIteration',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0, null=True)),
                ('hours', models.IntegerField(default=0, null=True)),
                ('defects', models.IntegerField(default=0, null=True)),
                ('iteration_name', models.CharField(default='unnamed iteration', max_length=25, null=True)),
                ('phase_name', models.CharField(default='unnamed phase', max_length=75)),
                ('project_name', models.CharField(default='unnamed project', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerPhase',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('is_open', models.BooleanField(default=False)),
                ('sloc', models.IntegerField(default=0, null=True)),
                ('hours', models.IntegerField(default=0, null=True)),
                ('defects', models.IntegerField(default=0, null=True)),
                ('phase_name', models.CharField(default='unnamed phase', max_length=25, null=True)),
                ('project_name', models.CharField(default='unnamed project', max_length=75)),
            ],
        ),
        migrations.DeleteModel(
            name='Iteration',
        ),
        migrations.DeleteModel(
            name='Phase',
        ),
    ]
