from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "is_author", "is_staff", "is_superuser"]
    list_filter = ("is_author", "is_staff")

admin.site.register(User, UserAdmin)