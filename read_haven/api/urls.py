from django.urls import path
from .views import BooksAPIView, BookAPIView, AuthorsAPIView, AuthorAPIView, CategoiresAPIView, CategoryAPIView

urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='books_api'),
    path('books/<int:pk>/', BookAPIView.as_view(), name='book_api'),
    path('authors/', AuthorsAPIView.as_view(), name='authors_api'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author_api'),
    path('categories/', CategoiresAPIView.as_view(), name='categories_api'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category_api'),
]