from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "jan": "Eat less carbs!",
    "feb": "Run a mile!",
    "march": "Eat something green!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challange", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"""
        <ul>
            {list_items}
        </ul>
    """
    return HttpResponse(response_data)


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
        challenge = monthly_challenges[month]
        response_data = f"<h1>{challenge}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound()