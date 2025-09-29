from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostHome.as_view(), name="post-home"),
    path('wszystkie', views.PostListing.as_view(), name="post-listing"),
    # path('<int:id>/<str:slug>', views.post, name="blog-post"),
    path('<slug:slug>', views.PostDetails.as_view(), name="post-details")
]