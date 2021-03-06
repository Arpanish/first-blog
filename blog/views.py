from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from django.contrib.auth import login, authenticate

from .models import Post
from django.contrib.auth.models import User
from .forms import LoginForm, signupForm, CreatePostForm


# function based view
def index(request):
    posts = Post.objects.all().order_by("-id")[:3]
    active = 'home'
    return render(request, 'index.html', {'posts': posts, 'active':active})

class PostList(View):
    active = 'li'
    template_name = 'blog/blog-list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(
            request, self.template_name, {
                'posts': posts, 'active': self.active}
        )

    def post(self, request, *args, **kwargs):
        search_str = request.POST.get("search_str")
        posts = Post.objects.filter(title__icontains=search_str)
        return render(
            request, self.template_name, {
                'posts': posts, 'active': self.active}
        )



 
def post_detail(request, id):
    posts = Post.objects.get(id=id)
    active = 'detail'
    return render(request, 'blog/blog-detail.html', {'posts':posts, 'active':active})



# class based views
class Login(View):
  
    template_name = 'login.html'
    form_class = LoginForm
    active = 'login'

    def get(self, request, *args, **kwargs):
       
        form = self.form_class()
          
        return render(request, self.template_name, {'active' : self.active, 'form' : form})  
     

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')


        return render(
            request, self.template_name, {'form' : form, 'active' : self.active})
    

class signup(View):

    template_name = 'signup.html'
    form_class = signupForm
    active = "signup"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'active' : self.active} )


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(
                username = username, email = email, password = password)
            authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')    
        return render(request, self.template_name, {'active' : self.active, 'form' : form}) 

class AddPost(View):
    template_name = "blog/add-post.html"
    form_class = CreatePostForm
    active = "addpost"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'active' : self.active})



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('post-list')

        return render(
            request, self.template_name, {'active' : self.active, 'form' : form})



def deletepost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post-list')  



class EditPost(View):

    template_name = 'blog/edit-post.html'
    form_class = CreatePostForm

    def get(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        return render(request, self.template_name, {'active': 'li', 'post': post})

    def post(self, request, id, *args, **kwargs):

        post = Post.objects.get(id=id)
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

        return redirect('index')


       


    

# Create your views here.
