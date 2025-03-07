from django.urls import path
from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('allbooks/', views.list_books, name= "list_books"),
    path('bookdetail/', LibraryDetailView.as_view(), name= "LibraryDetailView")

]