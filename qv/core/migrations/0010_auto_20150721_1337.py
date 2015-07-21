# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150721_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='timeVar',
            field=models.CharField(default=b'year', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='xVar',
            field=models.CharField(default=b'id', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='yVar',
            field=models.CharField(default=b'value', max_length=255, null=True, blank=True),
        ),
    ]
