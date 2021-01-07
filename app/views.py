from django.shortcuts import render
from django.http import HttpResponse

def app(request):
    return render(request, 'home/index.html')