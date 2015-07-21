# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150713_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='sheet',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='starting_row',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='file_field',
            field=models.FileField(upload_to=b'/home/alex/git/di-quick-vis/qv/data/%Y/%m/%d'),
        ),
    ]
