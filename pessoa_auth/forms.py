from django import forms
from pessoa_auth.models import CustomUser
from pessoa.forms import PessoaForm
from django.utils.text import ugettext_lazy as _


class UserCreationForm(forms.ModelForm):

	class Meta:
		model = CustomUser
		fields = ('cpf', 'data_nascimento')

	def save(self, commit=True):
		user = super().save(commit)
		user.set_password(self.cleaned_data['data_nascimento'].strftime('%d%m%Y'))
		if commit:
			user.save()
		return user

class UserChangeForm(PessoaForm):

	class Meta:
		model = CustomUser
		fields = ('nome', 'sobrenome', 'cpf', 'data_nascimento', 'is_active', 'is_superuser')

	def clean_password(self):
		return self.initial['password']