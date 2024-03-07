from django.shortcuts import render

from .models import BlogPost

# Blog home page - shows a list of the most recent articles
def home(request):
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-pub_date')[:10]

    data = {
        'posts': blog_posts
    }
    return render(request, 'blog/home.html', data)

# Blog Post detail page - shows a specific post
def blog_post_detail(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)

    data = {
        'post': blog_post
    }
    return render(request, 'blog/blog-post-detail.html', data)

