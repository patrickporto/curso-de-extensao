# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def migrate_professores(apps, schema_editor):
    Disciplina = apps.get_model('disciplina', 'Disciplina')
    for disciplina in Disciplina.objects.all():
        disciplina.professor_temp = disciplina.professor.first()
        disciplina.save()


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0003_auto_20140921_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='professor_temp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='professor', null=True),
            preserve_default=True,
        ),
        migrations.RunPython(migrate_professores),
        migrations.AlterField(
            model_name='disciplina',
            name='professor_temp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='professor', null=False),
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='professor',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='professor_temp',
            new_name='professor',
        ),
    ]
