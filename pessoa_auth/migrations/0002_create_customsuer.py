# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa_auth', '0001_initial'),
        ('pessoa', '0006_manual_cpf_unico'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('pessoa_ptr', models.OneToOneField(to='pessoa.Pessoa', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
            bases=('pessoa.pessoa', models.Model),
        ),
    ]
