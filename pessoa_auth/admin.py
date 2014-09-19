from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin
from pessoa_auth.models import CustomUser
from pessoa_auth.forms import UserChangeForm, UserCreationForm
from pessoa.admin import PessoaAdmin

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(PessoaAdmin, UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('cpf', 'nome_completo', 'data_nascimento', 'is_superuser',)
	list_filter = ('is_superuser', 'is_active',)
	fieldsets = (
		('Informações Pessoais', {
			'fields': ('nome', 'sobrenome','cpf', 'data_nascimento',),
		}),
		('Permissões', {
			'fields': ('is_superuser', 'is_active',),
		})
	)
	add_fieldsets = fieldsets

	search_fields = ('cpf', 'nome', 'sobrenome',)
	ordering = ('nome', 'sobrenome',)
	filter_horizontal = ()

admin.site.unregister(Group)