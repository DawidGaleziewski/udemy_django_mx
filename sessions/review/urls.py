from django.urls import path
from .views import ReviewList, AddReview, ReviewDetail
from .views import AddFavourite

urlpatterns = [
    path('add', AddReview.as_view(), name='review-add'),
    path('list', ReviewList.as_view(), name='review-list'),
    path('fav/<int:pk>', AddFavourite.as_view() ,name='review-favourite'),
    path('<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]