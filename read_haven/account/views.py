from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from book.models import Book, Author
from .models import User
from .forms import CustomUserCreationForm, BookForm, PhotoFormSet, ProfileForm
from .mixins import AuthorRequiredMixin

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account:login")
    template_name = "registration/signup.html"

class ProfileView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'registration/profile.html'

    def get_login_url(self):
        return reverse_lazy('account:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        context["orders"] = user.orders.filter(status='p')[:3]
        context["carts"] = user.cart.filter(status='p')[:3]

        return context

@login_required(login_url='account:login')
def add_to_orders(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='p')
    user = request.user
    if user.orders.filter(id=book.id).exists():
        user.orders.remove(book)
    else:
        user.orders.add(book)
    return redirect('book:book', book.slug)

@login_required(login_url='account:login')
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='p')
    user = request.user
    if user.cart.filter(id=book.id).exists():
        user.cart.remove(book)
        book.sell -= 1
        book.save()
    else:
        user.cart.add(book)
        book.sell += 1
        book.save()
    return redirect('book:book', book.slug)

class OrderBookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'registration/orders.html'

    def get_login_url(self):
        return reverse_lazy('account:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        context["orders"] = user.orders.filter(status='p')

        return context

class CartBookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'registration/cart.html'

    def get_login_url(self):
        return reverse_lazy('account:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        context["carts"] = user.cart.filter(status='p')

        return context

class BookCreateView(LoginRequiredMixin, AuthorRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'registration/new_book.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['photos'] = PhotoFormSet(self.request.POST, self.request.FILES)
        else:
            data['photos'] = PhotoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        author_exist = Author.objects.get(name=self.request.user.get_full_name())
        if author_exist == False:
            author_instance = Author()
            author_instance.name = self.request.user.get_full_name()
            author_instance.author_image = self.request.user.profile_image
            author_instance.save()
            form.instance.author = author_instance
        else:
            form.instance.author = Author.objects.get(name=self.request.user.get_full_name())
        
        photos = context['photos']
        self.object = form.save()
        if photos.is_valid():
            photos.instance = self.object
            photos.save()
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('account:my_books')

    def get_login_url(self):
        return reverse_lazy('account:login')

class MyBookListView(LoginRequiredMixin, AuthorRequiredMixin, ListView):
    model = Book
    template_name = 'registration/my_books.html'
    context_object_name = 'myBooks'

    def get_queryset(self):
        author_name = self.request.user.get_full_name()
        books = Book.objects.filter(author__name=author_name)
        return books
    
    def get_login_url(self):
        return reverse_lazy('account:login')
    
class BookUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'registration/update_book.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['photos'] = PhotoFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['photos'] = PhotoFormSet(instance=self.object)
        return data

    def get_queryset(self):
        slug = self.kwargs['slug']
        author_name = self.request.user.get_full_name()
        return Book.objects.filter(slug=slug, author__name=author_name)
    
    def form_valid(self, form):
        context = self.get_context_data()
        photos = context['photos']
        self.object = form.save()
        if photos.is_valid():
            photos.instance = self.object
            photos.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account:my_books')

    def get_login_url(self):
        return reverse_lazy('account:login')
    
class BookDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Book
    template_name = 'registration/book_delete.html'
    success_url = reverse_lazy("account:my_books")

    def get_queryset(self):
        author_name = self.request.user.get_full_name()
        books = Book.objects.filter(author__name=author_name)
        return books
    
    def get_login_url(self):
        return reverse_lazy('account:login')

class ProfileDetailView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile-view.html'
    form_class = ProfileForm
    success_url = reverse_lazy('account:dashboard')

    def get_object(self):
        return self.request.user