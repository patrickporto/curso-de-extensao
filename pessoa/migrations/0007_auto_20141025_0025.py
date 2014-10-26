# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0006_auto_20141025_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(unique=True, verbose_name='CPF', max_length=14),
        ),
    ]
