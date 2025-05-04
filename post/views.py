from django.shortcuts import render
from .models import Category , Post


# Main
def main(request):
    return render(request,'post/home.html')


# All Blogs
def blogs_list(request):
    post = Post.objects.all()
    return render(request,'post/blogs.html',{'posts' : post})