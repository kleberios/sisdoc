from django.contrib import admin
from .models import Setor, Equipamento, Ativo, Porta



admin.site.index_title = 'Sistema de Documentação de Ativos'
admin.site.site_header = 'Campus Senhor do Bonfim'

class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')

class EquipAdmin(admin.ModelAdmin):
    list_display = ['nome']

class AtivoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'local', 'modelo')

class PortaAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'porta', 'vlan', 'tag')

admin.site.register(Setor, SetorAdmin)
admin.site.register(Equipamento, EquipAdmin)
admin.site.register(Ativo, AtivoAdmin)
admin.site.register(Porta, PortaAdmin)
