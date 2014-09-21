# -*- encoding: utf-8 -*-
from django import forms
from pessoa.models import Pessoa, DocumentosPendentes
from localflavor.br.forms import BRCPFField


class PessoaChangeForm(forms.ModelForm):
    cpf = BRCPFField()

    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'data_nascimento', 'cpf', 'is_active', 'tipo',)


    def clean_password(self):
        return self.initial['password']


class PessoaCreationForm(PessoaChangeForm):

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['data_nascimento'].strftime('%d%m%Y'))
        if commit:
            user.save()
        return user


class DocumentosPendentesForm(forms.ModelForm):
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
    documentos = forms.MultipleChoiceField(choices=CHOICES_DOCUMENTOS, widget=forms.CheckboxSelectMultiple,
                                           required=False, label='Documentos Pendentes')

    class Meta:
        model = DocumentosPendentes
        fields = ('documentos',)