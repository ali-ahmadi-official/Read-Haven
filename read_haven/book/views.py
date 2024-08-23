from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from comment.mixins import CommentMixin
from .models import Book, Category, Author
from .mixins import CategoryMixin, BookConditionMixin, OrderBookMixin, CartBookMixin

class BookListView(CategoryMixin, BookConditionMixin, ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 10
    
    def get_queryset(self):
        books = Book.objects.filter(status='p')
        return books

class CategoryListView(CategoryMixin, ListView):
    model = Category
    context_object_name = "categories"
    
    def get_queryset(self):
        categories = Category.objects.filter(status=True)
        return categories

class CategoryBookListView(CategoryMixin, ListView):
    model = Category
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category, slug=slug, status=True)
        books = category.books_category.filter(status='p')
        return books
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["category"] = get_object_or_404(Category, slug=slug, status=True)
        return context

class AuthorListView(CategoryMixin, ListView):
    model = Author
    context_object_name = "authors"

class AuthorBookListView(CategoryMixin, ListView):
    model = Author
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        author = get_object_or_404(Author, slug=slug)
        books = author.books_author.filter(status='p')
        return books
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["author"] = get_object_or_404(Author, slug=slug)
        return context

class SimilarBooksListView(CategoryMixin, OrderBookMixin, CartBookMixin, CommentMixin, ListView):
    template_name = 'book/book_detail.html'
    context_object_name = 'similarbooks'

    def get_queryset(self):
        slug = self.kwargs['slug']
        book = get_object_or_404(Book, slug=slug)

        categories = book.category.filter(status=True)
        similarbooks = []
        for category in categories:
            similarbooks.extend(category.books_category.exclude(pk=book.pk).filter(status='p')[:5])
        return similarbooks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['book'] = get_object_or_404(Book, slug=slug)
        return context