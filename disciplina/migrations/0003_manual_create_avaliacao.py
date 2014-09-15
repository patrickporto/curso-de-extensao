# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_manual_create_aluno'),
        ('disciplina', '0002_manual_add_data_criacao_and_data_atualizacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nota', models.DecimalField(decimal_places=2, verbose_name='Nota', max_digits=5)),
                ('faltas', models.IntegerField(verbose_name='Faltas')),
                ('aluno', models.ForeignKey(to='pessoa.Aluno')),
                ('disciplina', models.ForeignKey(to='disciplina.Disciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
