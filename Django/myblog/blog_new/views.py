from django.shortcuts import render
"""from django.http import HttpResponse"""
from django.http import Http404
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404('Post Not Found')
    return render(request, 'post.html', {'post': post})
