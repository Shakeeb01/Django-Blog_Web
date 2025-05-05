from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from .models import Category , Post
from .forms import PostCreateForm,PostUpdateForm


# Main
def main(request):
    return render(request,'post/home.html')


# All Blogs and Searched blogs
def blogs_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(category__name__icontains=query)
        )
        return render(request,'post/blogs.html',{'posts':posts})
    else:
        posts = Post.objects.all()
        return render(request,'post/blogs.html',{'posts' : posts})




# Post Update and create view
def post_create_update_view(request, pk=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = PostUpdateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('all_blogs')
        else:
            form = PostUpdateForm(instance=post)
        context = {'form': form, 'type': 'update'}

    else:
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('all_blogs')
        else:
            form = PostCreateForm()
        context = {'form': form, 'type': 'create'}

    return render(request, 'post/create_update_blog.html', context)



# Post delete view
def delete_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('all_blogs')