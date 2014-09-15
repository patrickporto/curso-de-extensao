# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_manual_create_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='pessoa.Pessoa', auto_created=True)),
            ],
            options={
            },
            bases=('pessoa.pessoa',),
        ),
    ]
