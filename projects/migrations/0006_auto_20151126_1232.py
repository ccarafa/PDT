# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20151126_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerproject',
            name='construction_iteration_1',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='construction_iteration_2',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='construction_iteration_3',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='construction_phase',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='elaboration_phase',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='eleboration_iteration_1',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='eleboration_iteration_2',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='inception_iteration_1',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='inception_phase',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='transition_iteration_1',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='transition_iteration_2',
        ),
        migrations.RemoveField(
            model_name='managerproject',
            name='transition_phase',
        ),
    ]
