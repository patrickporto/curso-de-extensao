from django import forms
from pessoa.models import Pessoa, Aluno
from django_localflavor_br.forms import BRCPFField

class PessoaForm(forms.ModelForm):
    cpf = BRCPFField()
    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'data_nascimento', 'cpf',)


FOTOS = 1
CURRICULO = 2
HISTORICO_SUPERIOR = 3
RG = 4
TITULO_ELEITOR = 5
CERTIFICADO_RESERVISTA = 6
DIPLOMA_GRADUACAO = 7

CHOICES_DOCUMENTOS = (
    (FOTOS, '2 fotos 3x4',),
    (CURRICULO, 'Currículo',),
    (HISTORICO_SUPERIOR, 'Histórico Nível Superior',),
    (RG, 'Carteira Identidade',),
    (TITULO_ELEITOR, 'Título de Eleitor',),
    (CERTIFICADO_RESERVISTA, 'Certificado de Reservista',),
    (DIPLOMA_GRADUACAO, 'Diploma de Graduação',),
)


class AlunoForm(forms.ModelForm):
    documentos = forms.MultipleChoiceField(choices=CHOICES_DOCUMENTOS, widget=forms.CheckboxSelectMultiple,
                                           required=False, label='Documentos Pendentes')
    class Meta:
        model = Aluno
        fields = ('nome', 'sobrenome', 'data_nascimento', 'cpf', 'documentos',)