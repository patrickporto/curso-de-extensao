# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0005_manual_create_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(verbose_name='CPF', unique=True, max_length=14),
        ),
    ]
