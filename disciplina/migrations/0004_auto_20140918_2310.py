# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0003_manual_create_avaliacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'verbose_name_plural': 'Avaliações', 'verbose_name': 'Avaliação'},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='faltas',
            field=models.IntegerField(verbose_name='Faltas', default=0),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, verbose_name='Nota', max_digits=5, default=0),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=datetime.datetime(2014, 9, 18, 23, 10, 33, 143971)),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=datetime.datetime(2014, 9, 18, 23, 10, 33, 143971)),
        ),
    ]
