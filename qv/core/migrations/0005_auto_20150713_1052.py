# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150713_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, null=True, blank=True),
        ),
    ]
