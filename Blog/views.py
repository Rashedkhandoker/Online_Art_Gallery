from django.shortcuts import render
from .models import Blog
from .forms import BlogForm

# Create your views here.

def showBlog(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request, 'Blog/Blogs.html', context)

def insertBlog(request):
    form = BlogForm()
    message = ""
    if request.method == "POST":
        form = BlogForm(request.POST)
        message = "invalid input. Please try again"
        if form.is_valid():
            form.save()
            message="Blog is added"
            form=BlogForm()

    context = {
        'form':form,
        'message':message
    }

    return render(request, 'Blog/InsertBlog.html', context)
