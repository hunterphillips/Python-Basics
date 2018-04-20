# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# return HttpResponse('Hello from posts')  EXAMPLE response

from .models import Posts

# define views & response content
def index(request):
    # get all Posts, limit view to first 10
    posts = Posts.objects.all()[:10]
    # define 'content' to render
    context = {
      'title': 'Latest Posts',
      'posts': posts 
    }
    
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id = id)
    context = {
      "post": post
    }
    
    return render(request, 'posts/details.html', context)
