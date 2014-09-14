# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(to='pessoa.Pessoa', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('documentos', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=('pessoa.pessoa',),
        ),
    ]
