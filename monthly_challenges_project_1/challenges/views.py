from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def january(request):
    return HttpResponse("January")


def feb(request):
    return HttpResponse("February")