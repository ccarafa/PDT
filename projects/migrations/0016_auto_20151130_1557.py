# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20151127_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefectsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('defect_description', models.CharField(default=b'-', max_length=500)),
                ('defect_type', models.CharField(default=b'-', max_length=100)),
                ('project_name', models.CharField(default=b'-', max_length=75)),
                ('phase_name', models.CharField(default=b'-', max_length=75)),
                ('iteration_name', models.CharField(default=b'-', max_length=25)),
                ('username', models.CharField(default=b'-', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='estimate_yield',
            field=models.IntegerField(default=0),
        ),
    ]
