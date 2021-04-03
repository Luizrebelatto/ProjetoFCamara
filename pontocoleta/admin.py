from django.contrib import admin
from .models import PontosColeta

# Register your models here.


@admin.register(PontosColeta)
class ListaMaterialAdmin(admin.ModelAdmin):
    list_display = ('ponto_nome', 'ponto_cidade', 'ponto_uf')
    list_display_links = ('ponto_nome',)