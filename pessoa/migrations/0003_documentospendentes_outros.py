# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20140921_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentospendentes',
            name='outros',
            field=models.CharField(default='', max_length=255, verbose_name='Outros', blank=True),
            preserve_default=True,
        ),
    ]
