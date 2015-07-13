# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150713_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='data',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 10, 28, 52, 101019, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 7, 13, 10, 29, 5, 909019, tzinfo=utc), unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
