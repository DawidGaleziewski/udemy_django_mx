from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name="post-home"),
    path('wszystkie', views.post_listing, name="post-listing"),
    # path('<int:id>/<str:slug>', views.post, name="blog-post"),
    path('<slug:slug>', views.post_details, name="post-details")
]