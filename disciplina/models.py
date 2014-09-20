# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from pessoa.models import Aluno
from datetime import datetime

class Disciplina(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    limite_faltas = models.IntegerField(verbose_name='Limite de faltas')
    data_inicio = models.DateField(verbose_name='Data de início')
    data_termino = models.DateField(verbose_name='Data de término')
    professor = models.ManyToManyField(settings.AUTH_USER_MODEL)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=datetime.now())
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=datetime.now())

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    disciplina = models.ForeignKey(Disciplina)
    aluno = models.ForeignKey(Aluno)
    nota = models.DecimalField(verbose_name='Nota', decimal_places=2, max_digits=5, default=0)
    faltas = models.IntegerField(verbose_name='Faltas', default=0)

    def __str__(self):
        return "{0} - {1}".format(self.aluno, self.disciplina)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = 'Avaliações'
