from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging


# Create your views here.
posts = [
    {'id':1,'title':'post 1', 'content' : 'content of post 1' },
    {'id':2,'title':'post 2', 'content' : 'content of post 2' },
    {'id':3,'title':'post 3', 'content' : 'content of post 3' },
    {'id':4,'title':'post 4', 'content' : 'content of post 4' },
         
    ]
def index(request):
    blog_title="Latest Posts"
   
    return render(request,"index.html", {'blog_title': blog_title, 'posts':posts})


def detail(request, post_id):
    post= next((item for item in posts if item['id'] == int(post_id)), None)

    # for debugging......
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')

    return render(request,"detail.html",{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")