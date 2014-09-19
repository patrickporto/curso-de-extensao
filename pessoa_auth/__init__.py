from django.apps import AppConfig

class PessoaAuth(AppConfig):
	name = 'pessoa_auth'
	verbose_name='Autenticação'

default_app_config = 'pessoa_auth.PessoaAuth'