from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, UserProfile, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test


def list_books(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"template": book})


class LibraryDetailView(DetailView):
    model_name = Book
    template_name = "relationship_app/library_detail.html"
    custom_name = "book"



def register(request):
    form = UserCreationForm()

    return render(request, "relationship_app/register.html", {
        "form":form
    })



def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")