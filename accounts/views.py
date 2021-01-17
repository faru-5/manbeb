from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from .forms import SignUpForm
from django.contrib.messages import success


class Login(LoginView):
    template_name = "auth/login.html"
    success_url = "/"

    
class Logout(LogoutView):
    template_name = "home/about.html"


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            success(request, uname)
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html', {'form':form})
