from django.test import TestCase
from pessoa.models import Pessoa
from disciplina.models import Disciplina, Avaliacao
from datetime import date

class DisciplinaTest(TestCase):

    def setUp(self):
        self.professor = Pessoa()
        self.professor.nome = 'Fulano'
        self.professor.sobrenome = 'da Silva'
        self.professor.data_nascimento = date(1994, 1, 19)
        self.professor.cpf = '444.444.444-44'
        self.professor.tipo = Pessoa.PROFESSOR
        self.professor.save()

    def test_create_disciplina(self):
        disciplina = Disciplina()
        disciplina.nome = ''
        disciplina.limite_faltas = 10
        disciplina.data_inicio = date(2014, 1, 19)
        disciplina.data_termino = date(2014, 5, 19)
        disciplina.save()
        disciplina.professor.add(self.professor)

        self.assertGreater(Disciplina.objects.select_related('professor').count(), 0)


class AvaliacaoTest(TestCase):

    def setUp(self):
        self.professor = Pessoa()
        self.professor.nome = 'Fulano'
        self.professor.sobrenome = 'da Silva'
        self.professor.data_nascimento = date(1984, 1, 19)
        self.professor.cpf = '555.555.555-55'
        self.professor.tipo = Pessoa.PROFESSOR
        self.professor.save()

        self.disciplina = Disciplina()
        self.disciplina.nome = ''
        self.disciplina.limite_faltas = 10
        self.disciplina.data_inicio = date(2014, 1, 19)
        self.disciplina.data_termino = date(2014, 5, 19)
        self.disciplina.save()
        self.disciplina.professor.add(self.professor)

        self.aluno = Pessoa()
        self.aluno.nome = 'Fulaninho'
        self.aluno.sobrenome = 'de Souza'
        self.aluno.data_nascimento = date(1994, 1, 19)
        self.aluno.cpf = '111.111.111-11'
        self.aluno.tipo = Pessoa.ALUNO
        self.aluno.save()

    def test_create_nota(self):
        avaliacao = Avaliacao()
        avaliacao.disciplina = self.disciplina
        avaliacao.aluno = self.aluno
        avaliacao.faltas = 6
        avaliacao.nota = 8
        avaliacao.save()