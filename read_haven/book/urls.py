from django.urls import path
from comment.views import CommentCreateView, ReplyCommentCreateView, SubReplyCreateView
from .views import (BookListView, CategoryListView, CategoryBookListView, 
                    AuthorBookListView, AuthorListView, SimilarBooksListView)

app_name = "book"

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<slug:slug>/', SimilarBooksListView.as_view(), name='book'),
    path('books/<slug:slug>/comment/', CommentCreateView.as_view(), name='book-comment'),
    path('books/<slug:slug>/<int:id>/', ReplyCommentCreateView.as_view(), name='book-comment-reply'),
    path('books/<slug:slug>/reply/<int:id>/', SubReplyCreateView.as_view(), name='book-reply-reply'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<slug:slug>/', CategoryBookListView.as_view(), name='category'),

    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<slug:slug>/', AuthorBookListView.as_view(), name='author'),
]