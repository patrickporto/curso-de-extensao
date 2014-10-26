# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0005_auto_20140923_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(verbose_name='CPF', max_length=14),
        ),
    ]
