# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150721_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='json',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sheet',
            field=models.IntegerField(help_text=b'Starting at 0', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='starting_row',
            field=models.IntegerField(help_text=b'Starting at 0', null=True, blank=True),
        ),
    ]
