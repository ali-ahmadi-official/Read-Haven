from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from book.models import Book, Category

@require_http_methods(["GET", "POST"])
def search_book(request):
    categories = Category.objects.filter(status=True)[:5]

    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        books = Book.objects.filter(title__icontains=search_query)

        return render(request, 'search/search_book.html', {'query': search_query, 'books': books, 'categories': categories})
    else:
        return render(request, 'search/search_book.html', {'query': '', 'categories': categories})