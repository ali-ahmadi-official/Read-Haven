from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Book, Author, Category, Photo

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

class PhotoAdmin(admin.StackedInline):
    model = Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status"]

class BookAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]
    
    list_display = ["title", "categories", "author", "availability_and_price_validity", "status"]
    list_filter = ("author", "category", "availability", "status")
    search_fields = ("title", "description")

    actions = ["make_existent_book", "make_non_existent_book", "make_published", "make_in_the_review_queue"]

    def categories(self, obj):
        return ", ".join(category.title for category in obj.category.all())
    
    def book_publish_year_corrected(self, obj):
        return obj.book_publish_year_fuction()
    
    def availability_and_price_validity(self, obj):
        return obj.availability_and_price_validity()

    availability_and_price_validity.short_description = "price validity"
    book_publish_year_corrected.short_description = "book publish year"

    @admin.action(description="Mark selected books as Existent book")
    def make_existent_book(self, request, queryset):
        updated = queryset.update(availability="e")
        self.message_user(
            request,
            ngettext(
                "%d book was successfully marked as Existent book.",
                "%d books were successfully marked as Existent book.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    
    @admin.action(description="Mark selected books as Non-Existent book")
    def make_non_existent_book(self, request, queryset):
        updated = queryset.update(availability="n")
        self.message_user(
            request,
            ngettext(
                "%d book was successfully marked as Non-Existent book.",
                "%d books were successfully marked as Non-Existent book.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Mark selected books as Published")
    def make_published(self, request, queryset):
        updated = queryset.update(status="p")
        self.message_user(
            request,
            ngettext(
                "%d book was successfully marked as Published.",
                "%d books were successfully marked as Published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Mark selected books as In the review queue")
    def make_in_the_review_queue(self, request, queryset):
        updated = queryset.update(status="i")
        self.message_user(
            request,
            ngettext(
                "%d book was successfully marked as In the review queue.",
                "%d books were successfully marked as In the review queue.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)