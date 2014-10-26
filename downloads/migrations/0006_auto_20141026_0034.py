# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0005_monografias_para_monografia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivohistorico',
            options={'verbose_name': 'Hist\xf3rico de Downloads', 'verbose_name_plural': 'Hist\xf3rico de Downloads'},
        ),
        migrations.AlterField(
            model_name='arquivohistorico',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Data da A\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='arquivohistorico',
            name='ip',
            field=models.IPAddressField(verbose_name=b'Endere\xc3\xa7o IP'),
        ),
        migrations.AlterField(
            model_name='arquivohistorico',
            name='usuario',
            field=models.CharField(max_length=255, verbose_name=b'Usu\xc3\xa1rio'),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='arquivo',
            field=downloads.models.NewFileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='descricao',
            field=models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True),
        ),
    ]
