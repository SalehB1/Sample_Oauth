from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
class UserAdmin(UserAdmin):
    search_fields = ('phone', 'username', 'email')
    list_display = ('phone', 'email', 'username',  'is_verified', 'date_joined')
    date_hierarchy = ('date_joined')


admin.site.register(User, UserAdmin)
