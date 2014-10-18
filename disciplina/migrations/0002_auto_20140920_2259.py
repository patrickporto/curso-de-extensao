# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data_inicio', models.DateField(verbose_name='Data de início', default=django.utils.timezone.now)),
                ('data_termino', models.DateField(verbose_name='Data de término', default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='data_inicio',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='data_termino',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='periodo',
            field=models.ManyToManyField(to='disciplina.Periodo'),
            preserve_default=True,
        ),
    ]
