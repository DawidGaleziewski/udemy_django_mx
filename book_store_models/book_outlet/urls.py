from django.urls import path

from book_outlet import views

urlpatterns = [
    path('', views.index, name='book-store'),
    path('<int:book_id>', views.book_detail, name='book-detail'),
]