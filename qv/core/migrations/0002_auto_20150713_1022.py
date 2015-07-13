# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='content',
        ),
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
