from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required

from .models import BlogPost
from .forms import SendCountryForm, BlogPostForm

# Blog home page - shows a list of the most recent articles
def home(request):
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-pub_date')[:10]

    data = {
        'posts': blog_posts
    }
    return render(request, 'blog/home.html', data)

@permission_required('blog.add_blogpost', raise_exception=True)
def blog_post_add(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect(blog_post)

    # Otherwise, send an empty form
    else:
        form = BlogPostForm()

    return render(request, 'blog/blog-post-add.html', { 'form': form })

@permission_required('blog.change_blogpost', raise_exception=True)
def blog_post_change(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect(blog_post)

    # Otherwise, create a form using the blog_post
    else:
        form = BlogPostForm(instance=blog_post)

    return render(request, 'blog/blog-post-change.html', 
                     { 'form': form, 'post': blog_post })

# Blog Post detail page - shows a specific post
def blog_post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)

    data = {
        'post': blog_post
    }
    return render(request, 'blog/blog-post-detail.html', data)

@permission_required('blog.delete_blogpost', raise_exception=True)
def blog_post_delete(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        blog_post.delete()
        return redirect("blog:home")


    data = {
        'post': blog_post
    }
    return render(request, 'blog/blog-post-delete.html', data)
