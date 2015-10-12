from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',
                                         'phone_number', 'mobile_number',
                                         'zip_code', 'home_address',
                                         'bank_id_first', 'bank_id_last')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username','email', 'first_name', 'last_name',
                    'mobile_number', 'phone_number',
                    'is_staff')
    search_fields = ('username','email', 'first_name', 'last_name', 'mobile_number', 'phone_number')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

