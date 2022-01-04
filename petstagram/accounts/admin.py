from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from petstagram.accounts.models import PetstagramUser


@admin.register(PetstagramUser)
class PetstagramUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login',)}),
    )
