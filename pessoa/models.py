# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    sobrenome = models.CharField(max_length=255, verbose_name='Sobrenome')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', default=datetime.now())
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de atualização', default=datetime.now())

    def __str__(self):
        return self.nome_completo()

    def nome_completo(self):
        return "{0} {1}".format(self.nome, self.sobrenome)
    nome_completo.short_description = 'Nome completo'


class Contato(models.Model):
    TELEFONE = 'telefone'
    EMAIL = 'email'
    CHOICES_TIPO_CONTATO = (
        (TELEFONE, 'Telefone',),
        (EMAIL, 'Email',),
    )
    tipo = models.CharField(max_length=255, choices=CHOICES_TIPO_CONTATO, verbose_name='Tipo de Contato')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    pessoa = models.ForeignKey(Pessoa)

    def __str__(self):
        return "{0} - {1}".format(dict(self.CHOICES_TIPO_CONTATO)[self.tipo], self.descricao)

class Aluno(Pessoa):
    documentos = models.CharField(max_length=255, verbose_name='Documentos pendentes')


class Professor(Pessoa):
    class Meta:
        verbose_name_plural = 'Professores'