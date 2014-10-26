# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0009_auto_20141026_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='periodo',
        ),
        migrations.DeleteModel(
            name='Periodo',
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='situacao',
            field=models.CharField(default=b'cursando', max_length=255, verbose_name=b'Situa\xc3\xa7\xc3\xa3o', choices=[(b'cursando', b'Cursando'), (b'aprovado', b'Aprovado'), (b'reprovado por media', b'Reprovado por m\xc3\xa9dia'), (b'reprovado por faltas', b'Reprovado por faltas'), (b'reprovado por media e faltas', b'Reprovado por m\xc3\xa9dia e faltas')]),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='data_inicio',
            field=models.DateField(verbose_name=b'Data de in\xc3\xadcio'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='data_termino',
            field=models.DateField(verbose_name=b'Data de t\xc3\xa9rmino'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='limite_abonos',
            field=models.IntegerField(verbose_name=b'Limite de abonos'),
        ),
    ]
