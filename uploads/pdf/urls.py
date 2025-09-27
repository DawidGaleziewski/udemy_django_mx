from .views import UploadPDF2, PDFList
from django.urls import path

urlpatterns = [
    path('upload', UploadPDF2.as_view(), name='pdf_upload'),
    path('list', PDFList.as_view(), name='pdf_list'),
]