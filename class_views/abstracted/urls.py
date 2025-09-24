from .views import IndexView, RevDetail
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<id>', RevDetail.as_view(), name='detail')
]