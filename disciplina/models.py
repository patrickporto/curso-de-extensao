# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils import timezone
from pessoa.models import Pessoa


class AvaliacaoQuerySet(models.QuerySet):
    def aprovados(self):
        return self.filter(nota__gte=settings.BUSINESS['media_aprovacao'],
                           faltas__lte=models.F('disciplina__limite_faltas'))

    def reprovados(self):
        return self.filter(models.Q(nota__lt=settings.BUSINESS['media_aprovacao']) |
                           models.Q(faltas__gt=models.F('disciplina__limite_faltas')))


class AvaliacaoManager(models.Manager):
    def get_queryset(self):
        return AvaliacaoQuerySet(self.model, using=self._db)

    def aprovados(self):
        return self.get_queryset().aprovados()

    def reprovados(self):
        return self.get_queryset().reprovados()


class Periodo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Período")
    data_inicio = models.DateField(verbose_name='Data de início', default=timezone.now)
    data_termino = models.DateField(verbose_name='Data de término', default=timezone.now)

    def __unicode__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Disciplina')
    limite_faltas = models.IntegerField(verbose_name='Limite de faltas')
    periodo = models.ManyToManyField(Periodo)
    professor = models.ForeignKey(Pessoa, limit_choices_to={'tipo': Pessoa.PROFESSOR}, related_name='professor')
    aluno = models.ManyToManyField(Pessoa, limit_choices_to={'tipo': Pessoa.ALUNO}, related_name='alunos', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=timezone.now)

    def __unicode__(self):
        return self.nome

    def quant_alunos(self):
        return len(self.aluno.all())
    quant_alunos.short_description = "Quantidade de alunos"


class Avaliacao(models.Model):
    CURSANDO = 'cursando'
    APROVADO = 'aprovado'
    REPROVADO = 'reprovado'
    CHOICES_SITUACAO = (
        (CURSANDO, 'Cursando',),
        (APROVADO, 'Aprovado',),
        (REPROVADO, 'Reprovado'),
    )
    disciplina = models.ForeignKey(Disciplina)
    aluno = models.ForeignKey(Pessoa, limit_choices_to={'tipo': Pessoa.ALUNO})
    nota = models.DecimalField(verbose_name='Nota', decimal_places=2, max_digits=5, default=None, null=True, blank=True)
    faltas = models.IntegerField(verbose_name='Faltas', default=0)
    situacao = models.CharField(max_length=255, verbose_name='Situação', choices=CHOICES_SITUACAO, default=CURSANDO)

    objects = AvaliacaoManager()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.aluno, self.disciplina)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = 'Avaliações'


def disciplina_post_save(sender, instance, action, *args, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        Avaliacao.objects.filter(disciplina=instance).exclude(aluno=instance.aluno.all).delete()

        for aluno in instance.aluno.all():
            Avaliacao.objects.get_or_create(aluno=aluno, disciplina=instance)

models.signals.m2m_changed.connect(disciplina_post_save, sender=Disciplina.aluno.through)
