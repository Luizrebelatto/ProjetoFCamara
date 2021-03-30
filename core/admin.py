from django.contrib import admin
from .models import Relative, ListaMaterial, Material

# Register your models here.


@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    list_display = ('relative_parent', 'relative_name', 'relative_birth', 'relative_grade', 'relative_school')


@admin.register(ListaMaterial)
class ListaMaterialAdmin(admin.ModelAdmin):
    list_display = ('lista_nome',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('item_nome', 'item_quantidade',)


