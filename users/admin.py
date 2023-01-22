from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'date_joined', 'last_login')
    list_display_links = ('id', 'username')
    list_filter = ('id', 'username', 'is_staff', 'date_joined', 'last_login')
    search_fields = ('username',)
