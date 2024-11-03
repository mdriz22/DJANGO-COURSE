from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm


# Create your views here.

#static Demo Data ------------------------------------------------
# posts = [
#     {'id':1,'title':'post 1', 'content' : 'content of post 1' },
#     {'id':2,'title':'post 2', 'content' : 'content of post 2' },
#     {'id':3,'title':'post 3', 'content' : 'content of post 3' },
#     {'id':4,'title':'post 4', 'content' : 'content of post 4' },        
#     ]

def index(request):
    blog_title="Latest Posts"
    # getting Data from post model
    all_posts = Post.objects.all()
    paginator=Paginator(all_posts, 5)
    page_number= request.GET.get('page')
    page_obj= paginator.get_page(page_number)

    return render(request,"index.html", {'blog_title': blog_title, 'page_obj':page_obj})


def detail(request, slug):
    #static Data
    # post= next((item for item in posts if item['id'] == int(post_id)), None)

    # for debugging......
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')

    try:

        #getting data from model by  post id
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(Category = post.Category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")    

    return render(request,"detail.html",{'post':post , 'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"POST Data is { form.cleaned_data['name']} { form.cleaned_data['email']} { form.cleaned_data['message']}")
            #send email or save in database
            success_message="Your Email has been sent"
            return render(request,"contact.html",{'form':form , 'success_message':success_message})
        else:
            logger.debug('Form validation failure')   
        return render(request,"contact.html",{'form':form , 'name':name , 'email':email,'message':message})
        
    return render(request,"contact.html")


def about_view(request):
    about_content=AboutUs.objects.first().content
    return render(request,"about.html",{'about_content':about_content})