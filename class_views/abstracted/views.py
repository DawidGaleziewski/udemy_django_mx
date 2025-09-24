from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

# TemplateView allows us to define a template that will be used
class IndexView(TemplateView):
    template_name = "abstracted.html"

    # constructing context provided to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Django Class Views"
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class RevDetail(TemplateView):
    template_name = "details.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Review.objects.get(id=review_id)
        context["review"] = review
        return context