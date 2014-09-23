from django.db import models
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


class Arquivo(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    slug = AutoSlugField(populate_from='nome', unique=True)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    arquivo = models.FileField()
    downloads = models.IntegerField(verbose_name='Quantidade de downloads realizados', default=0)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('download', kwargs={'slug': self.slug})