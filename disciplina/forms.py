# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets
from disciplina.models import Disciplina

class DisciplinaForm(forms.ModelForm):
    professor = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.filter(tipo=get_user_model().PROFESSOR),
                                               widget=widgets.FilteredSelectMultiple(
                                                   verbose_name='Professores', is_stacked=False))
    class Meta:
        model = Disciplina
        fields = ('nome', 'limite_faltas', 'periodo', 'professor',)