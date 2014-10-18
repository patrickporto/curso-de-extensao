# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import datetime
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, default=datetime.date(2014, 9, 23), editable=False),
            preserve_default=False,
        ),
    ]
