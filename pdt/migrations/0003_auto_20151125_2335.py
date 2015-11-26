# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0002_auto_20151125_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='phases',
            name='projectname',
            field=models.CharField(default='unnamed project', max_length=75),
        ),
        migrations.AlterField(
            model_name='phases',
            name='defects',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='phases',
            name='hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='phases',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='phases',
            name='sloc',
            field=models.IntegerField(null=True),
        ),
    ]
