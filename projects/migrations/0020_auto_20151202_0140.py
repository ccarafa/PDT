# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_projectsdeveloper_is_started'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('defect_description', models.CharField(max_length=500, default='-')),
                ('defect_type', models.CharField(max_length=100, default='-')),
                ('project_name', models.CharField(max_length=75, default='-')),
                ('phase_name', models.CharField(max_length=75, default='-')),
                ('iteration_name', models.CharField(max_length=25, default='-')),
                ('username', models.CharField(max_length=128, default='-')),
            ],
        ),
        migrations.DeleteModel(
            name='DefectsList',
        ),
        migrations.AlterField(
            model_name='iteration',
            name='phase_name',
            field=models.CharField(max_length=200, default='-'),
        ),
    ]
