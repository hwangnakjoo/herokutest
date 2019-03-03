from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog_model
from .forms import BlogPost


def home(request):
    blogs = Blog_model.objects
    return render(request, 'home.html', {'blogs':blogs})


def detail(request, blog_model_id):
    blogapp_detail = get_object_or_404(Blog_model, pk=blog_model_id)
    return render(request, 'detail.html', {'blogdetail':blogapp_detail})


def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog_model()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.img = request.GET['image']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request):
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/blog/' + str(post.id))
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form}) 


def edit(request, blog_model_id):
    post = get_object_or_404(Blog_model, pk=blog_model_id)
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/blog/' + str(post.id))
    else:
        form = BlogPost(instance=post)
    return render(request, 'edit.html', {'form':form})