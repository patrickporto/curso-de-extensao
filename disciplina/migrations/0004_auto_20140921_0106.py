# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disciplina', '0003_auto_20140921_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='professor',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='professores', null=True),
            preserve_default=True,
        ),
    ]
