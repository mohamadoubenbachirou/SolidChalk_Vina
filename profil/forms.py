from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms 
from django.contrib.auth.models import User

class CustomUserChangeForm(UserChangeForm):
    class meta: 
        model=User
        fields=['Nom','email']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass 