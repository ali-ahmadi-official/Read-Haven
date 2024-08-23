from .models import Comment

class CommentMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book_slug = self.kwargs['slug']
        context['comments'] = Comment.objects.filter(book__slug=book_slug, status='p')
        return context