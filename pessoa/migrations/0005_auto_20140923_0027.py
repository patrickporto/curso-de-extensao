# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_auto_20140922_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentospendentes',
            name='outros',
            field=models.CharField(blank=True, default='', verbose_name='Outros', max_length=255, help_text='Por favor, use vírgula (,) como separador para definir multiplos documentos'),
        ),
    ]
