# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0002_arquivo_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoHistorico',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data da Ação')),
                ('ip', models.IPAddressField(verbose_name='Endereço IP')),
                ('usuario', models.CharField(verbose_name='Usuário', max_length=255)),
                ('arquivo', models.ForeignKey(to='downloads.Arquivo', verbose_name='Arquivo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
