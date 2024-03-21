from django.shortcuts import render, redirect, get_object_or_404

from .models import BlogPost
from .forms import SendCountryForm, BlogPostForm

# Blog home page - shows a list of the most recent articles
def home(request):
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-pub_date')[:10]

    data = {
        'posts': blog_posts
    }
    return render(request, 'blog/home.html', data)

def send_country(request):
    if request.method == "POST":
        form = SendCountryForm(request.POST)
        if form.is_valid():
            with open("countries.log", '+w') as f:
                f.write(form.cleaned_data['country'] + "\n")
            return redirect('/')

    # Otherwise, send an empty form
    else:
        form = SendCountryForm()

    return render(request, 'blog/send-country.html', { 'form': form })

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

