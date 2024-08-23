from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book

class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    profile_image = models.ImageField(default='default/user_default.jpg', upload_to='user_photos/')
    orders = models.ManyToManyField(Book, related_name='orders')
    cart = models.ManyToManyField(Book, related_name='cart')

    def __str__(self):
        return self.username
