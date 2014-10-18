# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0006_auto_20140921_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='situacao',
            field=models.CharField(choices=[('cursando', 'Cursando'), ('aprovado', 'Aprovado'), ('reprovado', 'Reprovado')], max_length=255, default='cursando', verbose_name='Situação'),
            preserve_default=True,
        ),
    ]
