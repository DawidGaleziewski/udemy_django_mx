from django.contrib import admin

# Register your models here.
from .models import Book, Author


# if we want to modify the admin panel. We can create our own view. Using custome class and by extending ModelAdmin
class BookAdmin(admin.ModelAdmin):
    # override admmin presentation for book here
    # readonly_fields = ("slug",)
    # this is how we can pre-populate the field
    prepopulated_fields = {"slug": ("title",)}

    # we add option for filtering the fields
    list_filter = ("rating",)

    list_display = ("title", "rating", "author")

# this will allow us to manage this resource in admin panel
admin.site.register(Book, BookAdmin)
admin.site.register(Author)