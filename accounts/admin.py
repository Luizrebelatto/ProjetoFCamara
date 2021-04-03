from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserForm, CustomUserChangeForm

from .models import CustomUser, Profile, Dependente


class UserCustomAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


@admin.register(CustomUser)
class CustomUserAdmin(UserCustomAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_donor')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_donor', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)


@admin.register(Dependente)
class ListaMaterialAdmin(admin.ModelAdmin):
    list_display = ('dependente_nome', 'dependente_nascimento',)
    list_display_links = ('dependente_nome',)
