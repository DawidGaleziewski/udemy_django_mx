from django.http import Http404
from django.shortcuts import render, get_object_or_404
from book_outlet.models import Book

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    return render(request, "index.html", {"books": all_books})

def book_detail(request, book_id:int):
    # there is also a shortcut for syntax below
    # get_object_or_404()
    try:
        book = Book.objects.get(id=book_id)
        return render(request, "book_detail.html", {"book": book})
    except:
        raise Http404("Book does not exist")