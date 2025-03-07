from django.urls import path
from . import views
from .views import book_detail, all_books


urlpatterns = [
    path('allbooks/', views.all_books, name= "allbooks"),
    path('bookdetail/', book_detail.as_view(), name= "bookdetail")

]