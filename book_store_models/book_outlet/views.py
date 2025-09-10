from django.shortcuts import render
from book_outlet.models import Book

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    return render(request, "index.html", {"books": all_books})

def book_detail(request, book_id:int):
    book = Book.objects.get(id=book_id)
    return render(request, "book_detail.html", {"book": book})