# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0007_avaliacao_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(null=True, verbose_name='Nota', decimal_places=2, default=None, max_digits=5),
        ),
    ]
