# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(verbose_name='Nome', max_length=255)),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('arquivo', models.FileField(upload_to='')),
                ('downloads', models.IntegerField(default=0, verbose_name='Quantidade de downloads realizados')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
