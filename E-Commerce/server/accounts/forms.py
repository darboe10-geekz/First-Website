from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CustomUser, UserProfile

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password", help_text="You can change the password using <a href=\"../password/\">this form</a>.")
    # password = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    is_active = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
        
    def clean_password(self):
        return self.initial["password"]
    
    
class UserProfileForm(forms.ModelForm):
    model = UserProfile
    fields = ('profile_picture', 'bio')
    
    # def clean_profile_picture(self):
    #     profile_picture = self.cleaned_data.get('profile_picture')
    #     if profile_picture and not profile_picture.name.lower().endswith(('.png', '.jpg', '.jpeg')):
    #         raise forms.ValidationError("Only .png, .jpg, and .jpeg files are allowed.")
    #     return profile_picture