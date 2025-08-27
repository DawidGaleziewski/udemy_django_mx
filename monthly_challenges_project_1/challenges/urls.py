from django.urls import path
from . import views

# URL config. Needs to be connect to url config. Requests will be routed here from main url config
urlpatterns = [
    path("january", views.january),
    path("feb", views.feb)
]
