from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AdminPasswordChangeForm
from pessoa_auth.models import CustomUser
from pessoa_auth.forms import UserChangeForm, UserCreationForm
from pessoa.admin import PessoaAdmin

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(PessoaAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('cpf', 'nome_completo', 'data_nascimento', 'is_superuser',)
	list_filter = ('is_superuser',)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
		})
	)

	search_fields = ('cpf', 'nome', 'sobrenome',)
	ordering = ('nome', 'sobrenome',)

admin.site.unregister(Group)