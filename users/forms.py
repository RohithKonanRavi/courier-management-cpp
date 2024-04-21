from django import forms
from .models import user

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['user_username', 'user_password', 'user_name', 'user_email', 'user_mobile']