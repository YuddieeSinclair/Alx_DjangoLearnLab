from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('allbooks/', views.list_books, name= "list_books"),
    path('bookdetail/', LibraryDetailView.as_view(), name= "LibraryDetailView"),
    path("register/", views.register, name= "register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name= 'logout'),
    path('Admin/', admin_view, name= "admin_view"),
    path('add_book/', add_book, name= "add_book"),
    path('edit_book/', edit_book, name= "edit_book"),
    path('delete_book/', delete_book, name= "delete_book"),
    

]