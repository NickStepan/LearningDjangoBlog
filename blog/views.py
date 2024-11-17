from django.shortcuts import render
from . import models

# Create your views here.

def post_list(request):
    posts = models.Post.objects.all()
    context = {
        "posts": posts

    }
    return render(request, "blog/post_list.html", context)

def post_details(request, pk):
    post = models.Post.objects.get(id=pk)
    context = {
        'post': post,
        'published_recently': post.published_recently()
    }

    return render(request, 'blog/post_details.html', context)

def author_posts(request, pk):
    author = models.Author.objects.get(id=pk)
    context = {
        'posts': author.post.all()
    }

    return render(request, 'blog/post_list.html', context)