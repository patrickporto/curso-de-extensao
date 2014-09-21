# -*- encoding: utf-8 -*-
from django.db import models
from pessoa.models import Pessoa
from django.utils import timezone

class Periodo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Período")
    data_inicio = models.DateField(verbose_name='Data de início', default=timezone.now)
    data_termino = models.DateField(verbose_name='Data de término', default=timezone.now)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Disciplina')
    limite_faltas = models.IntegerField(verbose_name='Limite de faltas')
    periodo = models.ManyToManyField(Periodo)
    professor = models.ForeignKey(Pessoa, limit_choices_to={'tipo': Pessoa.PROFESSOR}, related_name='professor')
    aluno = models.ManyToManyField(Pessoa, limit_choices_to={'tipo': Pessoa.ALUNO}, related_name='alunos')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=timezone.now)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    disciplina = models.ForeignKey(Disciplina)
    aluno = models.ForeignKey(Pessoa, limit_choices_to={'tipo': Pessoa.ALUNO})
    nota = models.DecimalField(verbose_name='Nota', decimal_places=2, max_digits=5, default=None, null=True, blank=True)
    faltas = models.IntegerField(verbose_name='Faltas', default=0)

    def __str__(self):
        return "{0} - {1}".format(self.aluno, self.disciplina)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = 'Avaliações'
