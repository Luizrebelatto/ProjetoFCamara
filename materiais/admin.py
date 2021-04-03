from django.contrib import admin
from .models import (
    ListaMaterial,
)


@admin.register(ListaMaterial)
class ListaMaterialAdmin(admin.ModelAdmin):
    list_display = ('nome',)