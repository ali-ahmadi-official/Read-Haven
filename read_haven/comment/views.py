from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from book.models import Book
from .models import Comment, Reply

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.user.is_superuser:
            form.instance.status = 'p'
        form.instance.book = Book.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('book:book', kwargs={'slug': self.kwargs.get('slug')})
    
    def get_login_url(self):
        return reverse_lazy('account:login')

class ReplyCommentCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.user.is_superuser:
            form.instance.status = 'p'
        form.instance.book = Book.objects.get(slug=self.kwargs.get('slug'))
        form.instance.comment = Comment.objects.get(id=self.kwargs.get('id'))
        form.instance.reply = None
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('book:book', kwargs={'slug': self.kwargs.get('slug')})
    
    def get_login_url(self):
        return reverse_lazy('account:login')

class SubReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ['content']
    template_name = "comment/reply_reply.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.user.is_superuser:
            form.instance.status = 'p'
        form.instance.book = Book.objects.get(slug=self.kwargs.get('slug'))
        form.instance.comment = None
        form.instance.reply = Reply.objects.get(id=self.kwargs.get('id'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('book:book', kwargs={'slug': self.kwargs.get('slug')})
    
    def get_login_url(self):
        return reverse_lazy('account:login')