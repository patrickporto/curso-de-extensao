# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(max_length=255, blank=True, verbose_name='Sobrenome'),
        ),
    ]
