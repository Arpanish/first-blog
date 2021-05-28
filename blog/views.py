from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.all().order_by("-id")[:3]
    print(posts)

   
    return render(request, 'index.html', {'posts': posts})

def postlist(request):
     posts = Post.objects.all()
     print(posts)
     return render(request, 'blog/blog-list.html', {'posts':posts})  


# Create your views here.
