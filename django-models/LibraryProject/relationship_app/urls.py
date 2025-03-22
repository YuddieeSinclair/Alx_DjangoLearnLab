from django.urls import path
from . import views
from .views import list_books, register, LibraryDetailView
from django.contrib.auth.views import LogoutView, LoginView
from admin_view import admin_dashboard


urlpatterns = [
    path('allbooks/', views.list_books, name= "list_books"),
    path('bookdetail/', LibraryDetailView.as_view(), name= "LibraryDetailView"),
    path("register/", views.register, name= "register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name= 'logout'),
    path('isadmin/', admin_dashboard, name="admin")
]