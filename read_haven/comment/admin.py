from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Comment, Reply

class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "book", "publish", "status"]
    list_filter = ("book", "status")

    actions = ["make_published", "make_in_the_review_queue"]

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

class ReplyAdmin(admin.ModelAdmin):
    list_display = ["content", "comment", "reply", "publish", "status"]
    list_filter = ("status",)

    actions = ["make_published", "make_in_the_review_queue"]

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

admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)