from django.contrib import admin
from .models import Post, Author, Tag


class PostTagInline(admin.TabularInline):
    model = Tag.posts.through
    extra = 1
    verbose_name = "Tag"
    verbose_name_plural = "Tags"

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostTagInline]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
