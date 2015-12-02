# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20151126_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerproject',
            name='construction_iteration_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='construction_iteration_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='construction_iteration_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='construction_phase',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='developers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='elaboration_phase',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='eleboration_iteration_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='eleboration_iteration_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='inception_iteration_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='inception_phase',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='project_name',
            field=models.CharField(default=b'-', max_length=120),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='transition_iteration_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='transition_iteration_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='managerproject',
            name='transition_phase',
            field=models.IntegerField(default=0),
        ),
    ]
