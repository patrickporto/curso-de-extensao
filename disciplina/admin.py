from django.contrib import admin
from disciplina.models import Disciplina, Avaliacao
from disciplina.forms import DisciplinaForm

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'limite_faltas', 'data_inicio', 'data_termino',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'professor__nome', 'professor__sobrenome',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    form = DisciplinaForm


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'nota', 'faltas')
    list_editable = ('nota', 'faltas', )
    search_fields = ('aluno__nome', 'aluno__sobrenome', 'disciplina__nome', 'disciplina__professor__nome', 'disciplina__professor__sobrenome', )