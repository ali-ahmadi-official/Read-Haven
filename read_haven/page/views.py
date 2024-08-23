from django.views.generic import ListView
from book.models import Book, Category
from account.models import User

class CategoryListView(ListView):
    model = Category
    template_name = "page/home.html"
    context_object_name = "categories"

    def get_queryset(self):
        categories = Category.objects.filter(status=True)[:5]
        return categories
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["best_books"] = Book.objects.filter(status='p')[:10]
        context["our_books"] = Book.objects.filter(author__name__in=[user.get_full_name() for user in User.objects.all()], status='p')[:10]
        return context