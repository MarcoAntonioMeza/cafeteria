from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'direccion', 'foto_perfil', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('direccion', 'foto_perfil')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('direccion', 'foto_perfil')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
