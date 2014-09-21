from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from pessoa.models import Pessoa, Contato, DocumentosPendentes
from pessoa.forms import PessoaChangeForm, PessoaCreationForm, DocumentosPendentesForm


class ContatoInline(admin.StackedInline):
    model = Contato
    extra = 0
    min_num = 1


class DocumentosPendentesInline(admin.StackedInline):
    model = DocumentosPendentes
    extra = 0
    min_num = 1
    form = DocumentosPendentesForm


@admin.register(Pessoa)
class PessoaAdmin(UserAdmin):
    list_display = ('get_full_name', 'cpf', 'data_nascimento', 'tipo', )
    list_display_links = ('get_full_name', 'cpf',)
    list_filter = ('tipo', 'is_active',)
    search_fields = ('nome', 'sobrenome', 'cpf',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    inlines = [DocumentosPendentesInline, ContatoInline]
    form = PessoaChangeForm
    add_form = PessoaCreationForm

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'sobrenome', 'cpf', 'data_nascimento',),
        }),
        ('Permissões', {
            'fields': ('tipo', 'is_active',),
        })
    )
    add_fieldsets = fieldsets
    ordering = ('nome', 'sobrenome',)
    filter_horizontal = ()

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, DocumentosPendentesInline) and (not obj or obj.tipo != obj.ALUNO):
                continue
            yield inline.get_formset(request, obj), inline

    class Media:
        js = ('js/django.jquery.js', 'js/jquery.inputmask.min.js', 'js/django.inputmask.js',)


admin.site.unregister(Group)