from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "jan": "Eat less carbs!",
    "feb": "Run a mile!",
    "march": "Eat something green!",
    "april": None
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months":  months})

def monthly_challenge_by_number(request, month: int):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound()
    
    month_name = months[month - 1]
    # reverse uses a tag name to access whole path
    # good practice is to use reverse whenever we redirect
    redirect_path = reverse("month-challange", args=[month_name])
    # return monthly_challenge(request, month_name)
    return HttpResponseRedirect(redirect_path)


# must be named same as in dynamic route declaration <month>
def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]

        # we can use render to parse template to string and send response in http response in one go
        return render(request, "challenges/challenge.html", {
            "body_text" : challenge_text,
            "month_name": month,
        })

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # we cant use render here, as we want to send 404 status as well
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
        # raise Http404() # another way to return error page. This will AUTOMATICCALLY find a 404.html and return it