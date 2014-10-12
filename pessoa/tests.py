# -*- encoding: utf-8 -*-
from django.test import TestCase
from datetime import date
from pessoa.models import Pessoa, Contato

class PessoaTest(TestCase):

    def test_create_funcionario(self):
        pessoa = Pessoa()
        pessoa.nome = 'Fulano'
        pessoa.sobrenome = 'da Silva'
        pessoa.data_nascimento = date(1994, 1, 19)
        pessoa.cpf = '111.111.111-11'
        pessoa.tipo = Pessoa.FUNCIONARIO
        pessoa.save()
        contato_1 = Contato.objects.create(
            tipo=Contato.TELEFONE,
            descricao='(00)0000-0000',
            pessoa=pessoa
        )
        contato_2 = Contato.objects.create(
            tipo=Contato.EMAIL,
            descricao='fulano@email.com',
            pessoa=pessoa
        )

    def test_create_aluno(self):
        aluno = Pessoa()
        aluno.nome = 'Fulano'
        aluno.sobrenome = 'da Silva'
        aluno.data_nascimento = date(1994, 1, 19)
        aluno.cpf = '222.222.222-22'
        aluno.tipo = Pessoa.FUNCIONARIO
        aluno.save()
        contato_1 = Contato.objects.create(
            tipo=Contato.TELEFONE,
            descricao='(00)0000-0000',
            pessoa=aluno
        )
        contato_2 = Contato.objects.create(
            tipo=Contato.EMAIL,
            descricao='fulano@email.com',
            pessoa=aluno
        )

    def test_create_professor(self):
        professor = Pessoa()
        professor.nome = 'Fulano'
        professor.sobrenome = 'da Silva'
        professor.data_nascimento = date(1994, 1, 19)
        professor.cpf = '333.333.333-33'
        professor.tipo = Pessoa.PROFESSOR
        professor.save()
        contato_1 = Contato.objects.create(
            tipo=Contato.TELEFONE,
            descricao='(00)0000-0000',
            pessoa=professor
        )
        contato_2 = Contato.objects.create(
            tipo=Contato.EMAIL,
            descricao='fulano@email.com',
            pessoa=professor
        )
