from django.test import TestCase
from pessoa.models import Professor
from disciplina.models import Disciplina
from datetime import date

class DisciplinaTest(TestCase):

    def setUp(self):
        self.professor = Professor()
        self.professor.nome = 'Fulano'
        self.professor.sobrenome = 'da Silva'
        self.professor.data_nascimento = date(1994, 1, 19)
        self.professor.cpf = '111.111.111-11'
        self.professor.save()

    def test_create_disciplina(self):
        disciplina = Disciplina()
        disciplina.nome = ''
        disciplina.limite_faltas = 10
        disciplina.data_inicio = date(2014, 1, 19)
        disciplina.data_termino = date(2014, 5, 19)
        disciplina.save()
        disciplina.professor.add(self.professor)

        self.assertTrue(disciplina.pk)
        self.assertGreater(Disciplina.objects.select_related('professor').count(), 0)