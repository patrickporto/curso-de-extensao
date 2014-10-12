# -*- encoding: utf-8 -*-
from pessoa.models import Pessoa


class CustomBackend(object):
    def authenticate(self, username=None, password=None):
        if len(username) == 11:
            username = "{0}.{1}.{2}-{3}".format(username[0:3], username[3:6], username[6:9], username[9:11])
        customuser = Pessoa.objects.filter(cpf=username).first()
        if not customuser or not customuser.check_password(password):
            return None
        return customuser

    def get_user(self, user_id):
        try:
            return Pessoa.objects.get(pk=user_id)
        except Pessoa.DoesNotExist:
            return None
