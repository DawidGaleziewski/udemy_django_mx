from django.db.models import Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from book_outlet.models import Book

# Create your views here.
def index(request):
    # order_by is done on sql query level
    all_books = Book.objects.all().order_by("-rating")
    # we dont want to re declare the query. This way this will be cached and we hit db only once
    total_books = all_books.count()
    average_rating = round(all_books.aggregate(average_rating=Avg("rating"))["average_rating"], 2)
    return render(request, "index.html", {
        "books": all_books,
        "total_books": total_books,
        "average_rating": average_rating,
    })

def book_detail(request, slug:str):
    # there is also a shortcut for syntax below
    # get_object_or_404()
    try:
        book = Book.objects.get(slug=slug)
        return render(request, "book_detail.html", {"book": book})
    except:
        raise Http404("Book does not exist")