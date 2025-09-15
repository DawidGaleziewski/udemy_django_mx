import datetime

from django.shortcuts import render
from dataclasses import dataclass

from blog.models import Post


# Create your views here.
def post_listing(request):
    posts = Post.objects.all()
    return render(request, "blog/blog_listing.html", {"posts": posts})

def post_details(request,  slug: str):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/blog_details.html", {"post": post, "authors": post.authors.all() })

def post_home(request):
    # this is actually not as bad for performance as it seems. As django will CONVERT all of this into SQl syntax. That is, it will only select 3 resaults
    posts = Post.objects.all().order_by("-created_on")[:3]
    return render(request, "blog/blog_listing.html", {"posts": posts})