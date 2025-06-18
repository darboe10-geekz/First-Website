from django.contrib import admin
from .models import CustomUser, UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    class Meta:
        model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)



