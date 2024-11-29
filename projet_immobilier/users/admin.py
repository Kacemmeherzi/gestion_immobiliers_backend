from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import UserProfile
class CustomUserAdmin(UserAdmin):
    # Add all fields
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # Define the fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # Add search capabilities
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # Add filters
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register the new UserAdmin
admin.site.register(User, CustomUserAdmin)
# Register your models here.
admin.site.register(UserProfile)