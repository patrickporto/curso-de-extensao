# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets
from disciplina.models import Disciplina
from pessoa.models import Professor

class DisciplinaForm(forms.ModelForm):
    professor = forms.ModelMultipleChoiceField(queryset=Professor.objects.all(),
                                               widget=widgets.FilteredSelectMultiple(
                                                   verbose_name='Professores', is_stacked=False))
    class Meta:
        model = Disciplina
        fields = ('nome', 'limite_faltas', 'data_inicio', 'data_termino', 'professor',)