# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_manual_create_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='data_atualizacao',
            field=models.DateTimeField(verbose_name='Data de atualização', default=datetime.datetime(2014, 9, 14, 23, 28, 24, 736533), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='data_criacao',
            field=models.DateTimeField(verbose_name='Data de criação', default=datetime.datetime(2014, 9, 14, 23, 28, 24, 736533), auto_now_add=True),
            preserve_default=True,
        ),
    ]
