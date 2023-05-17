from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# admin.site.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('phone','address')
admin.site.register(CustomUser, CustomUserAdmin)
