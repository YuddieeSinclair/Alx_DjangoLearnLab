from django.shortcuts import render,redirect
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


from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login


def register(request):
    form = UserCreationForm()

    return render(request, "relationship_app/registration/register.html", {
        "form":form
    })