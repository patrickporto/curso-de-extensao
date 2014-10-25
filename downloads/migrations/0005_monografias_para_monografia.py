# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0004_monografia_nome'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Monografias',
            new_name='Monografia',
        ),
    ]
