from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
# define data entities here

# () is a way to extand a class in python. We extand class Models this way
class Book(models.Model):
    # all oficialy suported field types: https://docs.djangoproject.com/en/5.2/ref/models/fields/
    # id is created automatically for each entry
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    # this defines how things are stringified for object. Similar to java
    # if we add a method we dont need to run migration again. Only if we change the structure of the db fsdfsdf sdfsdf sdf sdfsdfsd fsdf sdf sdf sdf sdf sdf sd
    def __str__(self):
        return f"{self.title} - {self.rating} - {self.author}"

    # this is build in django method that we can override. We can call it inside our template to get the url for the book
    def get_absolute_url(self):
        url = reverse("book-detail", args=[self.slug])
        return url

    ## we can override the save() method
    def save(self, *args, **kwargs):
        # build in slugify method changes the title into a slug
        self.slug = slugify(self.title)

        # super extends build in save mnethods. We pass in arfs and kewywords
        super().save(*args, **kwargs)
