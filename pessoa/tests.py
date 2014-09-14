from django.test import TestCase
from datetime import date
from pessoa.models import Pessoa

class PessoaTest(TestCase):

    def test_create_pessoa(self):
        pessoa = Pessoa()
        pessoa.nome = 'Fulano'
        pessoa.sobrenome = 'da Silva'
        pessoa.data_nascimento = date(1994, 1, 19)
        pessoa.cpf = '111.111.111-11'
        pessoa.telefone = '(00)0000-0000'
        pessoa.email = 'fulano@email.com'
        pessoa.save()