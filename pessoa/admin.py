from django.contrib import admin
from pessoa.models import Pessoa, Contato, Aluno
from pessoa.forms import PessoaForm, AlunoForm

class ContatoInline(admin.StackedInline):
    model = Contato
    extra = 0
    min_num = 1

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento')
    list_display_links = ('nome_completo', 'cpf',)
    search_fields = ('nome', 'sobrenome', 'cpf',)
    inlines = [ContatoInline]
    form = PessoaForm
    class Media:
        js = ('js/django.jquery.js', 'js/jquery.inputmask.min.js', 'js/django.inputmask.js',)

@admin.register(Aluno)
class Aluno(PessoaAdmin):
    form = AlunoForm