# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0006_manual_cpf_unico'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Funcionario',
        ),
    ]
