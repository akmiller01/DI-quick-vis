# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150713_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file_field',
            field=models.FileField(upload_to=b'/home/alex/git/DI-quick-vis/qv/data/%Y/%m/%d'),
        ),
    ]
