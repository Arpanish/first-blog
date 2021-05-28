from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.all()
    print(posts)

   
    return render(request, 'index.html', {'posts': posts})

# Create your views here.
