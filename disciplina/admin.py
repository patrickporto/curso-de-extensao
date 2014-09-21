from django.contrib import admin
from disciplina.models import Disciplina, Avaliacao, Periodo
from disciplina.forms import DisciplinaForm

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'limite_faltas', )
    list_display_links = ('nome',)
    search_fields = ('nome', 'professor__nome', 'professor__sobrenome',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    list_filter = ('periodo__nome',)
    form = DisciplinaForm


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'nota', 'faltas')
    list_editable = ('nota', 'faltas', )
    search_fields = ('aluno__nome', 'aluno__sobrenome', 'disciplina__nome', 'disciplina__professor__nome', 'disciplina__professor__sobrenome', )
    list_filter = ('disciplina__periodo__nome', 'disciplina__nome',)


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_termino',)
    list_editable = ('data_inicio', 'data_termino',)