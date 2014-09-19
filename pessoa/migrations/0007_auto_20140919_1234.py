# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0006_manual_cpf_unico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='pessoa_ptr',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2014, 9, 19, 12, 34, 59, 626122), verbose_name='Data de atualização'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 19, 12, 34, 59, 626069), verbose_name='Data de criação', auto_now_add=True),
        ),
    ]
