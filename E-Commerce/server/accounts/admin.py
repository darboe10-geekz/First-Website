from django.contrib import admin
from .models import CustomUser, UserProfile
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    
    list_display = ('email', 'first_name', 'last_name','is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'permissions')}),
        # ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    
    
    class Meta:
        model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)



