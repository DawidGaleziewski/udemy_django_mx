from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm2
from .models import Review

# Create your views here.

def index(request):
    if request.method == "POST":
        # this fills the form with posted data
        form = ReviewForm2(request.POST)
        # entered_username = request.POST.get("name")

        # is_valid will validate inputs. But also populate clean data with values
        if form.is_valid():
            new_review = Review(
                name = form.cleaned_data["name"],
                review = form.cleaned_data["review"],
                rating = form.cleaned_data["rating"]
            )
            new_review.save()
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