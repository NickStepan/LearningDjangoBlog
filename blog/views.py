from django.shortcuts import render
from . import models

# Create your views here.

def post_list(request):
    posts = models.Post.objects.all()
    context = {
        "posts": posts

    }
    return render(request, "blog/post_list.html", context)