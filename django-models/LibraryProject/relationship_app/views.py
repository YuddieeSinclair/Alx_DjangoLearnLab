from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, Book

def list_books(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"template": book})


class LibraryDetailView(DetailView):
    model_name = Book
    template_name = "relationship_app/library_detail.html"
    custom_name = "book"