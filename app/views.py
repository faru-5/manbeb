from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def app(request):
    books = Book.objects.all()
    return render(request, 'home/index.html', {"books":books})