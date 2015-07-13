# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150713_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField(max_length=255, unique=True, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file_field', models.FileField(upload_to=b'/home/alex/git/DI-quick-vis/qv/data/%Y/%m/%d')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
