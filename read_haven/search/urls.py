from django.urls import path
from .views import search_book

app_name = "search"

urlpatterns = [
    path('books/', search_book, name='search'),
]