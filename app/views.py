from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView

def app(request):
    books = Book.objects.all()
    return render(request, 'home/index.html', {"books":books})

def singleBook(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'manbeb/single.html', {'id':id})

class SingleBook(DetailView):
    model = Book
    template_name = 'manbeb/single.html'