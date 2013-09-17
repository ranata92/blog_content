from blog.models import Post
from django.views.generic import ListView, DetailView


class PostMixin(object):
    model = Post

class PostList(PostMixin, ListView):
    paginate_by = 10

class PostDetail(PostMixin, DetailView):
    pass
