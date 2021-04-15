from django.shortcuts import render
from .models import Post
from users.models import Mail
from django.contrib.auth.models import User


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})