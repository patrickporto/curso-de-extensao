# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0008_auto_20141026_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='abonos',
            field=models.IntegerField(default=0, verbose_name=b'Abonos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='data_inicio',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Data de in\xc3\xadcio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='data_termino',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Data de t\xc3\xa9rmino'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='limite_abonos',
            field=models.IntegerField(default=0, verbose_name=b'Limite de abonos'),
            preserve_default=True,
        ),
    ]
