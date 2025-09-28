from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Review
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

class AddReview(CreateView):
    model = Review
    fields = '__all__'
    template_name = "review/add_review.html"
    success_url = "/reviews/list"

class ReviewList(ListView):
    model = Review
    template_name = "review/review_list.html"
    context_object_name = "reviews"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fav_id = self.request.session.get("favourite")
        context["fav_id"] = fav_id
        return context

class ReviewDetail(DetailView):
    model = Review
    template_name = "review/review_detail.html"
    context_object_name = "review"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # is is safe to access this data by .get. Otherwise if this data does not exist python will throw a error
        is_favourite = self.request.session.get("favourite") == self.object.id
        context["is_favourite"] = is_favourite
        return context


class AddFavourite(View):
    def post(self, request, pk):
        # pk = request.POST.get("pk")
        review = Review.objects.get(pk=pk)
        # django ads  default session handling
        # django under the hood makes sure also that thsi data gets add to the database
        # when assigning things to session. Django will automatically serialize it to a JSON if possible
        request.session["favourite"] = review.id
        url = reverse('review-detail', args=[pk])
        return HttpResponseRedirect(url)