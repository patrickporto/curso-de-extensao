# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('nome', models.CharField(verbose_name='Nome', max_length=255)),
                ('sobrenome', models.CharField(verbose_name='Sobrenome', max_length=255)),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=14)),
                ('data_criacao', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True, default=django.utils.timezone.now)),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=django.utils.timezone.now)),
                ('tipo', models.IntegerField(choices=[(1, 'Funcionário'), (2, 'Professor'), (3, 'Aluno')], verbose_name='Tipo de pessoa', max_length=255)),
                ('is_active', models.BooleanField(verbose_name='Ativo', default=True)),
            ],
            options={
                'verbose_name': 'Pessoa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tipo', models.CharField(choices=[('telefone', 'Telefone'), ('email', 'Email')], verbose_name='Tipo de Contato', max_length=255)),
                ('descricao', models.CharField(verbose_name='Descrição', max_length=255)),
                ('pessoa', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentosPendentes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('documentos', models.CharField(verbose_name='Documentos pendentes', max_length=255)),
                ('pessoa', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Documentos pendentes de aluno',
                'verbose_name_plural': 'Documentos pendentes de aluno',
            },
            bases=(models.Model,),
        ),
    ]
