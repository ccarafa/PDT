# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20151202_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='defect',
            name='injected_iteration',
            field=models.CharField(max_length=128, default='-'),
        ),
        migrations.AddField(
            model_name='defect',
            name='injected_phase',
            field=models.CharField(max_length=128, default='-'),
        ),
    ]
