# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0007_avaliacao_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='situacao',
            field=models.CharField(default=b'cursando', max_length=255, verbose_name=b'Situa\xc3\xa7\xc3\xa3o', choices=[(b'cursando', b'Cursando'), (b'aprovado', b'Aprovado'), (b'reprovado', b'Reprovado')]),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='data_atualizacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Data de atualiza\xc3\xa7\xc3\xa3o', auto_now=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(related_name=b'professor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data_inicio',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Data de in\xc3\xadcio'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data_termino',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Data de t\xc3\xa9rmino'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='nome',
            field=models.CharField(max_length=255, verbose_name=b'Per\xc3\xadodo'),
        ),
    ]
