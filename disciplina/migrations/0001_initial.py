# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Nota', default=0)),
                ('faltas', models.IntegerField(verbose_name='Faltas', default=0)),
                ('aluno', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(verbose_name='Nome', max_length=255)),
                ('limite_faltas', models.IntegerField(verbose_name='Limite de faltas')),
                ('data_inicio', models.DateField(verbose_name='Data de início')),
                ('data_termino', models.DateField(verbose_name='Data de término')),
                ('data_criacao', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True, default=django.utils.timezone.now)),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=django.utils.timezone.now)),
                ('professor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='disciplina',
            field=models.ForeignKey(to='disciplina.Disciplina'),
            preserve_default=True,
        ),
    ]
