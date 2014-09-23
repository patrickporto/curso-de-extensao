from django.contrib import admin
from downloads.models import Arquivo

@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug',)
    readonly_fields = ('downloads',)