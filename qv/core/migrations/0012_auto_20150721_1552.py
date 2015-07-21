# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150721_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='sheet',
            field=models.IntegerField(default=0, help_text=b'Starting at 0', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='starting_row',
            field=models.IntegerField(default=0, help_text=b'Starting at 0', null=True, blank=True),
        ),
    ]
