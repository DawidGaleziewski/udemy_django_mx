from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

monthly_challenges = {
    "jan": "Eat less carbs!",
    "feb": "Run a mile!",
    "march": "Eat something green!"
}

# must be named same as in dynamic route declaration <month>
def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound()