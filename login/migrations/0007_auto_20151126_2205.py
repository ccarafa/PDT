# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_developeriteration_developerphase_manageriteration_managerphase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeveloperIteration',
        ),
        migrations.DeleteModel(
            name='DeveloperPhase',
        ),
        migrations.DeleteModel(
            name='ManagerIteration',
        ),
        migrations.DeleteModel(
            name='ManagerPhase',
        ),
    ]
