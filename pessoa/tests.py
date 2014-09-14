from django.test import TestCase
from datetime import date
from pessoa.models import Pessoa, Contato, Aluno

class PessoaTest(TestCase):

    def test_create_pessoa(self):
        pessoa = Pessoa()
        pessoa.nome = 'Fulano'
        pessoa.sobrenome = 'da Silva'
        pessoa.data_nascimento = date(1994, 1, 19)
        pessoa.cpf = '111.111.111-11'
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

        self.assertTrue(pessoa)
        self.assertTrue(contato_1)
        self.assertTrue(contato_2)


class AlunoTest(TestCase):

    def test_create_aluno(self):
        aluno = Aluno()
        aluno.nome = 'Fulano'
        aluno.sobrenome = 'da Silva'
        aluno.data_nascimento = date(1994, 1, 19)
        aluno.cpf = '111.111.111-11'
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

        self.assertTrue(aluno)
        self.assertTrue(contato_1)
        self.assertTrue(contato_2)