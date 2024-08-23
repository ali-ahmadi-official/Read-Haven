from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')
    slug = AutoSlugField(populate_from="name", unique=True)
    author_image = models.ImageField(upload_to="author_photos/", default="default/author_default.jpg")

    def __str__(self):
        return self.name

class CategoryManager(models.Manager):
    def status(self):
        return self.filter(status=True)

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", unique=True)
    status = models.BooleanField(default=True)
    category_image = models.ImageField(upload_to="category_photos/", default="default/category_default.jpg")
    objects = CategoryManager()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Book(models.Model):
    AVAILABILITY_CHOICES = (
        ("e", "Existent book"),
        ("n", "Non-existent book")
    )

    PRICE_VALIDITY_CHOICES = (
        ("n", "Non-free"),
        ("f", "Free")
    )

    TYPE_OF_BOOK_CHOICES = (
        ("p", "Paper book"),
        ("e", "Electronic book")
    )

    STATUS_CHOICES = (
        ("i", "In the review queue"),
        ("p", "Published")
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    category = models.ManyToManyField(Category, related_name="books_category")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books_author")
    cover_image = models.ImageField(upload_to="book_photos/", default="default/book_default.png")
    book_publish_year = models.IntegerField(help_text="Please enter the publication year (e.g., 2024)")
    availability = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES, default="e", help_text="If the 'Non-existent book' option is selected, 'Out Of Stock' will be displayed in the product price section.")
    price_validity = models.CharField(max_length=1, choices=PRICE_VALIDITY_CHOICES, default="n", help_text="The product can only be priced if the 'Non-free' option is selected")
    price = models.CharField(max_length=20, help_text="based on US dollars")
    type_of_book = models.CharField(max_length=1, choices=TYPE_OF_BOOK_CHOICES, default="p")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="i")
    publish = models.DateTimeField(default=timezone.now)
    sell = models.IntegerField(default=0)

    class Meta:
        ordering = ['-sell']

    def __str__(self):
        return self.title
    
    def book_publish_year_fuction(self):
        if self.book_publish_year < 0:
            self.book_publish_year = 0
        else:
            self.book_publish_year = str(self.book_publish_year)
            if len(self.book_publish_year) < 4:
                self.book_publish_year = "0"
        return int(self.book_publish_year)

    def availability_and_price_validity(self):
        if self.availability == "n":
            self.price = "Out Of Stock"
        elif self.availability == "e":
            if self.price_validity == "f":
                self.price = "Free"
            else:
                try:
                    self.price = round(float(self.price), 2)
                    if self.price < 0:
                        self.price = "Invalid Price"
                except ValueError:
                    self.price = "Invalid Price"
        else:
            raise ValueError("Invalid availability value")
        return self.price

class Photo(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="photos")
    photos = models.ImageField(upload_to="book_photos/")