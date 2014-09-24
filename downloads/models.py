from django.db import models
from django.db.models import Q
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse

class ArquivoQuerySet(models.QuerySet):
    def pesquisa(self, query):
        if not query:
            return self
        return self.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))



class Arquivo(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    slug = AutoSlugField(populate_from='nome', unique=True)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    arquivo = models.FileField()
    downloads = models.IntegerField(verbose_name='Quantidade de downloads realizados', default=0)

    objects = ArquivoQuerySet.as_manager()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('download', kwargs={'slug': self.slug})

    def registre(self, pessoa, ip):
        if pessoa.is_anonymous():
            usuario = 'Anônimo'
        else:
            usuario = str(pessoa)
        ArquivoHistorico.objects.create(usuario=usuario, arquivo=self, ip=ip)


class ArquivoHistorico(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da Ação")
    arquivo = models.ForeignKey(Arquivo, verbose_name='Arquivo')
    ip = models.IPAddressField(verbose_name='Endereço IP')
    usuario = models.CharField(max_length=255, verbose_name="Usuário")

    def __str__(self):
        return "[{2}][{0}] {1}: {3}".format(self.data, self.arquivo, self.ip, self.usuario)

    class Meta:
        verbose_name = 'Histórico de Downloads'
        verbose_name_plural = verbose_name