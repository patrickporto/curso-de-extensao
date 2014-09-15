# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_manual_create_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome', max_length=255)),
                ('limite_faltas', models.IntegerField(verbose_name='Limite de faltas')),
                ('data_inicio', models.DateField(verbose_name='Data de início')),
                ('data_termino', models.DateField(verbose_name='Data de término')),
                ('professor', models.ManyToManyField(to='pessoa.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
