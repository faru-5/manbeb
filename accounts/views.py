from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


class Login(LoginView):
    template_name = "auth/login.html"
    success_url = "/"

    
class Logout(LogoutView):
    template_name = "home/about.html"

    
def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("login")
    
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form':form})

