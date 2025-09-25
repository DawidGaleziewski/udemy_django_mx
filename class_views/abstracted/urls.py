from .views import ReviewListClass, RevDetail
from django.urls import path

urlpatterns = [
    path('', ReviewListClass.as_view(), name='index'),
    # it is important to name this eaither pk or slug, for django DetailView to query by this param
    path('detail/<pk>', RevDetail.as_view(), name='detail')
]