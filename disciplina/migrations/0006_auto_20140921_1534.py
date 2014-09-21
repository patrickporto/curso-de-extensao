# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0005_auto_20140921_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='aluno',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='alunos', null=True),
        ),
    ]
