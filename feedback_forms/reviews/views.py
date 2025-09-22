from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm2
from .models import Review
from django.views import View

# Create your views here.

def index(request):
    if request.method == "POST":
        # this fills the form with posted data
        form = ReviewForm2(request.POST)
        # entered_username = request.POST.get("name")

        # is_valid will validate inputs. But also populate clean data with values
        if form.is_valid():
            # new_review = Review(
            #     name = form.cleaned_data["name"],
            #     review = form.cleaned_data["review"],
            #     rating = form.cleaned_data["rating"]
            # )
            # new_review.save()
            # when using model form. We can simply save right to db here
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm2()

    reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html', {
        "form": form,
        "reviews": reviews
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')


# some views can be defined as class
# convention is to add View but we dont have to
# we extand View class
class ReviewView(View):
    # class allows us to define different methods for the same view
    def get(self, request):
        form = ReviewForm2()
        reviews = Review.objects.all()
        return render(request, 'reviews/reviews.html', {
            "form": form,
            "reviews": reviews
        })

    def post(self, request):
        form = ReviewForm2(request.POST)
        reviews = Review.objects.all()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, 'reviews/reviews.html', {
            "form": form,
            "reviews": reviews
        })