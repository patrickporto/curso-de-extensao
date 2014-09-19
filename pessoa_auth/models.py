from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext as _
from pessoa.models import Pessoa


class CustomUserManager(BaseUserManager):
	def create_user(self, cpf, data_nascimento, password=None):
		if not cpf:
			raise ValueError(_('Usuários devem ter CPF'))

		user = self.model(
			cpf=cpf,
			data_nascimento=data_nascimento
		)

		if not password:
			password = str(data_nascimento).replace("/", "")

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, cpf, data_nascimento, password):
		if not cpf:
			raise ValueError(_('Usuários devem ter CPF'))

		user = self.create_user(
			cpf, 
			data_nascimento, 
			password
		)
		user.is_superuser = True
		user.save(using=self._db)
		return user



class CustomUser(Pessoa, AbstractBaseUser):
	USERNAME_FIELD = 'cpf'
	REQUIRED_FIELDS = ['data_nascimento']

	is_superuser = models.BooleanField(default=False, verbose_name='Funcionário')
	is_active = models.BooleanField(default=True, verbose_name='Ativo')

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_superuser

	objects = CustomUserManager()

	def get_full_name(self):
		return self.nome_completo()

	def get_short_name(self):
		return self.nome

	def __str__(self):
		return self.cpf

	class Meta:
		verbose_name = 'Usuário'