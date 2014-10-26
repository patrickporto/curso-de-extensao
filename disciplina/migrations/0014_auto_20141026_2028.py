# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0013_auto_20141026_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='situacao',
            field=models.CharField(default=b'cursando', max_length=255, verbose_name=b'Situa\xc3\xa7\xc3\xa3o', choices=[(b'cursando', b'Cursando'), (b'aprovado', b'Aprovado'), (b'reprovado por grau', b'Reprovado por grau'), (b'reprovado por frequ\xc3\xaancia', b'Reprovado por frequ\xc3\xaancia'), (b'reprovado por grau e frequencia', b'Reprovado por grau e frequ\xc3\xaancia')]),
        ),
    ]
