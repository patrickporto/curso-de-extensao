# -*- encoding: utf-8 -*-
from django.contrib import admin
from downloads.models import Arquivo, ArquivoHistorico

@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug',)
    readonly_fields = ('downloads',)

@admin.register(ArquivoHistorico)
class ArquivoHistoricoAdmin(admin.ModelAdmin):
    list_display = ('data', 'arquivo', 'usuario', 'ip',)
    list_display_links = None
    search_fields = ('arquivo__nome', 'ip', 'usuario',)
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(ArquivoHistoricoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
