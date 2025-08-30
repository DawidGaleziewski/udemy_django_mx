from django.urls import path
from . import views

# URL config. Needs to be connect to url config. Requests will be routed here from main url config
urlpatterns = [
    path("", views.index),
    # django will attempt to convert value to int. And if not possible it will go to next request
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challange")
]
