from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'city', 'phone')
    list_filter = ('id', 'email', 'city', 'phone')
    search_fields = ('id', 'email', 'city', 'phone')
