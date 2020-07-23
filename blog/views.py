from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse


# Create your views here.

def index(request):
    myposts = Blog.objects.all()
    return render(request, 'blog/index.html', {'allposts': myposts})


def blogpost(request, id):
    post = Blog.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html', {'post': post})
