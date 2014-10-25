# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0003_arquivohistorico'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Arquivo',
            new_name='Monografias',
        ),
    ]
