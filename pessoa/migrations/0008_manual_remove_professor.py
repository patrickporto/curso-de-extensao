# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0007_manual_remove_funcionario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Professor',
        ),
    ]
