from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='reviews'),
    path('class-view', views.ReviewView.as_view(), name='reviews-class'),
    path("thank-you", views.thank_you, name="thank-you")
]