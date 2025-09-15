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
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)