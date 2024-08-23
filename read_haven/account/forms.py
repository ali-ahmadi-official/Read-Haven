from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from book.models import Book, Photo
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'cover_image', 'book_publish_year', 'type_of_book',
                  'availability', 'price_validity', 'price']

PhotoFormSet = inlineformset_factory(Book, Photo, fields=['photos'], extra=5)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_image", "username", "first_name", "last_name", "email"]