from django.contrib import admin
from django.urls import path

import pages.views as pages_views

urlpatterns = [
    path('', pages_views.home, name='home'),
    path('about/', pages_views.about, name='about',),
    path('contact/', pages_views.contact, name='contact'),
]
