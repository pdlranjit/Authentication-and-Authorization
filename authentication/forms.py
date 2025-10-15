from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=['username','email','phone_no','location','college_name','password1','password2']

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)