from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog-listing"),
    path('<int:id>/<str:slug>', views.post, name="blog-post")
]