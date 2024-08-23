from django.shortcuts import get_object_or_404
from .models import Book, Category

class CategoryMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(status=True)[:5]
        return context

class BookConditionMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_books"] = self.model.objects.filter(status='p').count()
        context["free_books"] = self.model.objects.filter(price_validity='f').count()
        return context

class OrderBookMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']

        user = self.request.user
        book = get_object_or_404(Book, slug=slug)
        is_in_orders = user.orders.filter(id=book.id).exists() if user.is_authenticated else False

        context["is_in_orders"] = is_in_orders
        return context

class CartBookMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']

        user = self.request.user
        book = get_object_or_404(Book, slug=slug)
        is_in_cart = user.cart.filter(id=book.id).exists() if user.is_authenticated else False

        context["is_in_cart"] = is_in_cart
        return context