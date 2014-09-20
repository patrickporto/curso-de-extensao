from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from pessoa.models import Pessoa, Contato
from pessoa.forms import PessoaChangeForm, PessoaCreationForm


class ContatoInline(admin.StackedInline):
    model = Contato
    extra = 0
    min_num = 1


@admin.register(Pessoa)
class PessoaAdmin(UserAdmin):
    list_display = ('get_full_name', 'cpf', 'data_nascimento', 'tipo', )
    list_display_links = ('get_full_name', 'cpf',)
    list_filter = ('tipo', 'is_active',)
    search_fields = ('nome', 'sobrenome', 'cpf',)
    readonly_fields = ('data_criacao', 'data_atualizacao',)
    inlines = [ContatoInline]
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


    class Media:
        js = ('js/django.jquery.js', 'js/jquery.inputmask.min.js', 'js/django.inputmask.js',)


admin.site.unregister(Group)