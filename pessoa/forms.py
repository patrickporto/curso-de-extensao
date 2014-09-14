from django import forms
from pessoa.models import Pessoa
from django_localflavor_br.forms import BRCPFField

class PessoaForm(forms.ModelForm):
    cpf = BRCPFField()
    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'data_nascimento', 'cpf',)