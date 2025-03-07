from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import *

def all_books(request):
    book = Book.objects.all()
    return render(request, "list_books.html", {"template": book})


class book_detail(DetailView):
    model_name = Book
    template_name = "library_detail.html"
    custom_name = "book"