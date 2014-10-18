# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0004_auto_20140921_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(verbose_name='Nota', default=None, max_digits=5, blank=True, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.CharField(verbose_name='Disciplina', max_length=255),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='nome',
            field=models.CharField(verbose_name='Período', max_length=255),
        ),
    ]
