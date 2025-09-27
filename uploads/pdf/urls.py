from .views import UploadPDF
from django.urls import path

urlpatterns = [
    path('upload', UploadPDF.as_view(), name='pdf_upload'),
]