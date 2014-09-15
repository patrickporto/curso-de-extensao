from django.contrib import admin
from disciplina.models import Disciplina
from disciplina.forms import DisciplinaForm

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'limite_faltas', 'data_inicio', 'data_termino',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'professor__nome', 'professor__sobrenome',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    form = DisciplinaForm