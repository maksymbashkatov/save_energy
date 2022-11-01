from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # List of CustomUser model fields
    # ('id', 'email', 'role', 'organization_project')

    # List of users form
    list_display = ('id', 'email', 'role', 'organization_project')
    search_fields = ('organization_project',)

    ordering = ('email',)

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
