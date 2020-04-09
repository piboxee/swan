from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             published_date__year=year,
                             published_date__month=month,
                             published_date__day=day)

    context = {
        'post': post
    }

    return render(request, 'blog/post/detail.html', context)
