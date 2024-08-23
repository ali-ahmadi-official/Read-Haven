from django.db import models
from django.utils import timezone
from book.models import Book
from account.models import User

class Comment(models.Model):
    STATUS_CHOICES = (
        ("i", "In the review queue"),
        ("p", "Published")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user", default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments_book", default=None)
    content = models.CharField(max_length=800)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="i")

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-publish']

class ReplyManager(models.Manager):
    def status(self):
        return self.filter(status='p')

class Reply(models.Model):
    STATUS_CHOICES = (
        ("i", "In the review queue"),
        ("p", "Published")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies_user", default=None)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies_comment", null=True, blank=True, default=None)
    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies_reply", null=True, blank=True, default=None)
    content = models.CharField(max_length=800)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="i")
    objects = ReplyManager()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "replies"
        ordering = ['-publish']