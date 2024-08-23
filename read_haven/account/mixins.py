from django.http import Http404

class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_author:
            raise Http404
        return super().dispatch(request, *args, **kwargs)