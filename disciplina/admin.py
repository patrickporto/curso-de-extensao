from django.contrib import admin
from disciplina.models import Disciplina, Avaliacao, Periodo
from disciplina.forms import DisciplinaForm


def atualizar_situacao(modeladmin, request, queryset):
    # Aprovar os alunos com nota igual ou superior a média de aprovação e faltas igual ou inferior ao limte
    queryset.aprovados().update(situacao=Avaliacao.APROVADO)
    # Reprovar os alunos com nota inferior a média de aprovação e faltas superior ao limte
    queryset.reprovados().update(situacao=Avaliacao.REPROVADO)

atualizar_situacao.short_description = "Atualizar situação dos alunos selecionados"


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'limite_faltas', 'quant_alunos',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'professor__nome', 'professor__sobrenome',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    list_filter = ('periodo__nome',)
    form = DisciplinaForm


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'nota', 'faltas', 'situacao',)
    list_editable = ('nota', 'faltas', )
    search_fields = ('aluno__nome', 'aluno__sobrenome', 'disciplina__nome', 'disciplina__professor__nome', 'disciplina__professor__sobrenome', )
    list_filter = ('disciplina__periodo__nome', 'disciplina__nome',)
    actions = [atualizar_situacao]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_termino',)
    list_editable = ('data_inicio', 'data_termino',)