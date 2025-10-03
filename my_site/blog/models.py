from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    posts = models.ManyToManyField("Post", related_name="authors")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    posts = models.ManyToManyField("Post", related_name="tags", blank=True)
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(max_length=250, unique=True, null=False, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to="posts/", null=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_authors_names(self):
        author_string = ""
        authors = self.authors.all()
        authors_count = authors.count()
        for index, author in enumerate(authors):
            author_string += f"{author.get_full_name()}"
            if index < authors_count - 1:
                author_string += ", "
        return author_string


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)