from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # Home Page: Shows a list of recent articles
    path('', views.home, name='home'),

    path('send-country/', views.send_country),

    # BlogPost Views:
    #   detail - information about a specific blog post
    path('post/add/', views.blog_post_add, name='post-add'),
    path('post/<int:post_id>/', views.blog_post_detail, name='post-detail'),
    path('post/<int:post_id>/change/', views.blog_post_change, name='post-change'),

]
