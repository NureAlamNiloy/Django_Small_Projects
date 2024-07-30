from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_no', 'password1', 'password2')
        
class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email',  'password')
