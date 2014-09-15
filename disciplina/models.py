from django.db import models
from pessoa.models import Professor
from datetime import datetime

class Disciplina(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    limite_faltas = models.IntegerField(verbose_name='Limite de faltas')
    data_inicio = models.DateField(verbose_name='Data de início')
    data_termino = models.DateField(verbose_name='Data de término')
    professor = models.ManyToManyField(Professor)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=datetime.now())
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=datetime.now())

    def __str__(self):
        return self.nome