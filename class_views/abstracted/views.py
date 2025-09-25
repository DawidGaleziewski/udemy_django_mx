from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Review

# TemplateView allows us to define a template that will be used
# class IndexView(TemplateView):
#     template_name = "abstracted.html"
#
#     # constructing context provided to the template
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Django Class Views"
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# DetailView class will use pk or 'slug' dynamic route param to get the data
class RevDetail(DetailView):
    template_name = "details.html"
    context_object_name = "review"
    model = Review

# one thing to remember is that in temlate this will be shown as object_list
class ReviewListClass(ListView):
    model = Review
    template_name = "abstracted.html"
    # we can however change object list to a diffrent name
    context_object_name = "reviews"

    # if we however want to filter some of the items, we can do it here
    def get_queryset(self):
        base_queryset = super().get_queryset()
        # we could override it here
        # base_queryset.filter(rating__gte=4)
        return base_queryset