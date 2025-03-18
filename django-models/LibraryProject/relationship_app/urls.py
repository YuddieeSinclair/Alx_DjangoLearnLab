from django.urls import path
from . import views
from .views import list_books, register, LibraryDetailView
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('allbooks/', views.list_books, name= "list_books"),
    path('bookdetail/', LibraryDetailView.as_view(), name= "LibraryDetailView"),
    path("register/", views.register, name= "register"),
    path('login/', LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/registration/logout.html'), name= 'logout'),
]