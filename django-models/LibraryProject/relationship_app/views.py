from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, UserProfile, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required


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



#Admin view
def is_admin(user):
    return user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

#Libriarian view
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


#Member view
def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, "relationship_app/list_book.html")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request):
    return render(request, "relationship_app/list_book.html")



@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return render(request, "relationship_app/list_book.html")