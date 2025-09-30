import datetime

from django.shortcuts import render
from dataclasses import dataclass

from blog.models import Post
from django.views.generic import ListView, DetailView, TemplateView


class PostListing(ListView):
    model = Post
    template_name = "blog/blog_listing.html"
    context_object_name = "posts"
    ordering = ["-created_on"]

class PostDetails(DetailView):
    model = Post
    template_name = "blog/blog_details.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = self.object.authors.all()
        return context

class PostHome(ListView):
    template_name = "blog/blog_home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-created_on"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data