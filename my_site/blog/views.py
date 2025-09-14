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
    return render(request, "blog/blog_details.html", {"post": post})