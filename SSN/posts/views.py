from django.shortcuts import render
from .models import Post


def posts_list_view(request):
    all_posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {'all_posts': all_posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_details.html', {'post': post})
