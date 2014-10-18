# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_documentospendentes_outros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentospendentes',
            old_name='pessoa',
            new_name='aluno',
        ),
    ]
