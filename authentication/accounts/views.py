from django.shortcuts import render, redirect
from .form import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def send_otp(request):
    data = request.data


def home(request):
    return render(request, "home.html")

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LoginView(LoginView):
    authentication_form = CustomUserLoginForm
    template_name = 'login.html'






