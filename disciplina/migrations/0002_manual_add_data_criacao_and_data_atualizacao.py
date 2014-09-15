# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=datetime.datetime(2014, 9, 15, 0, 4, 38, 41157)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=datetime.datetime(2014, 9, 15, 0, 4, 38, 40157)),
            preserve_default=True,
        ),
    ]
