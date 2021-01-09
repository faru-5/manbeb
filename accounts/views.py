from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class Login(LoginView):
    template_name = "auth/login.html"
    success_url = "/"

    
class Logout(LogoutView):
    template_name = "home/about.html"

    

