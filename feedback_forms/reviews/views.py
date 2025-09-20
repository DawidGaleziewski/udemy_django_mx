from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # entered_username = request.POST.get("name")

        # is_valid will validate inputs. But also populate clean data with values
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    form = ReviewForm()
    return render(request, 'reviews/reviews.html', {
        "form": form,
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')