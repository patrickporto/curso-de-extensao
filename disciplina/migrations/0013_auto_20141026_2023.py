# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0012_auto_20141026_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='situacao',
            field=models.CharField(default=b'Cursando', max_length=255, verbose_name=b'Situa\xc3\xa7\xc3\xa3o', choices=[(b'Cursando', b'Cursando'), (b'Aprovado', b'Aprovado'), (b'Reprovado por Grau', b'Reprovado por grau'), (b'Reprovado por Frequ\xc3\xaancia', b'Reprovado por frequ\xc3\xaancia'), (b'Reprovado por Grau e Frequ\xc3\xaancia', b'Reprovado por grau e frequ\xc3\xaancia')]),
        ),
    ]
