# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0007_auto_20141025_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='descricao',
            field=models.CharField(max_length=255, verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='documentospendentes',
            name='outros',
            field=models.CharField(default=b'', help_text=b'Por favor, use v\xc3\xadrgula (,) como separador para definir multiplos documentos', max_length=255, verbose_name=b'Outros', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_atualizacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Data de atualiza\xc3\xa7\xc3\xa3o', auto_now=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='tipo',
            field=models.IntegerField(max_length=255, verbose_name=b'Tipo de pessoa', choices=[(1, b'Funcion\xc3\xa1rio'), (2, b'Professor'), (3, b'Aluno')]),
        ),
    ]
