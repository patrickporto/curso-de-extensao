# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0004_manual_add_data_criacao_and_data_atualizacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='pessoa.Pessoa', serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=('pessoa.pessoa',),
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterField(
            model_name='aluno',
            name='documentos',
            field=models.CharField(verbose_name='Documentos pendentes', max_length=255),
        ),
        migrations.AlterField(
            model_name='contato',
            name='descricao',
            field=models.CharField(verbose_name='Descrição', max_length=255),
        ),
        migrations.AlterField(
            model_name='contato',
            name='tipo',
            field=models.CharField(choices=[('telefone', 'Telefone'), ('email', 'Email')], verbose_name='Tipo de Contato', max_length=255),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(verbose_name='CPF', max_length=14),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=datetime.datetime(2014, 9, 18, 23, 10, 33, 117969)),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=datetime.datetime(2014, 9, 18, 23, 10, 33, 117969)),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(verbose_name='Nome', max_length=255),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(verbose_name='Sobrenome', max_length=255),
        ),
    ]
