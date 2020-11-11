from django.contrib import admin
from usuarios.models.usuario_model import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)