from django.shortcuts import render
from book_outlet import models

# Create your views here.
def index(request):
    all_books = models.Book.objects.all()
    return render(request, "index.html", {"books": all_books})