# -*- coding: utf-8 -*-

from django.contrib import admin
from disciplina.models import Disciplina, Avaliacao
from disciplina.forms import DisciplinaForm


def atualizar_situacao(modeladmin, request, queryset):
    queryset.aprovados().update(situacao=Avaliacao.APROVADO)
    queryset.reprovados_media().update(situacao=Avaliacao.REPROVADO_MEDIA)
    queryset.reprovados_falta().update(situacao=Avaliacao.REPROVADO_FALTA)
    queryset.reprovados_media().reprovados_falta().update(situacao=Avaliacao.REPROVADO_MEDIA_FALTA)

atualizar_situacao.short_description = "Atualizar situação dos alunos selecionados"


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor', 'limite_faltas', 'limite_abonos', 'quant_alunos', 'data_inicio', 'data_termino')
    list_display_links = ('nome',)
    search_fields = ('nome', 'professor__nome', 'professor__sobrenome',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    form = DisciplinaForm


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'nota', 'faltas', 'abonos', 'situacao',)
    list_editable = ('nota', 'faltas', 'abonos',)
    list_display_links = None
    search_fields = ('aluno__nome', 'aluno__sobrenome', 'disciplina__nome', 'disciplina__professor__nome', 'disciplina__professor__sobrenome', )
    list_filter = ('disciplina__nome',)
    actions = [atualizar_situacao]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(AvaliacaoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
