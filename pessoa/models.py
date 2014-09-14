from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    sobrenome = models.CharField(max_length=255, verbose_name='Sobrenome')
    data_nascimento = models.DateField(verbose_name='Data de nscimento')
    cpf = models.CharField(max_length=14, verbose_name='CPF')

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
        return "{0}: {1}".format(self.tipo, self.descricao)