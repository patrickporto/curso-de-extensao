# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disciplina', '0002_auto_20140920_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='aluno',
            field=models.ManyToManyField(related_name='alunos', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='professor',
            field=models.ManyToManyField(related_name='professores', to=settings.AUTH_USER_MODEL),
        ),
    ]
