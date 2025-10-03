import datetime

from django.shortcuts import render
from dataclasses import dataclass

from blog.models import Post
from django.views.generic import ListView, DetailView, TemplateView
from .forms import CommentForm
from django.views import View


class PostListing(ListView):
    model = Post
    template_name = "blog/blog_listing.html"
    context_object_name = "posts"
    ordering = ["-created_on"]

class PostDetails(View):
    # model = Post
    # template_name = "blog/blog_details.html"
    # context_object_name = "post"

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs["slug"])
        context = {
            "post": post,
            "comments": post.comments.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/blog_details.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comments": post.comments.all(),
            "comment_form": form
        }
        if form.is_valid():
            # creates a model instance so we can add a post later
            form_model_instance = form.save(commit=False)
            form_model_instance.post = post
            form_model_instance.save()
            return render(request, "blog/blog_details.html", context)

        return render(request, "blog/blog_details.html", context)

class PostHome(ListView):
    template_name = "blog/blog_home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-created_on"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data