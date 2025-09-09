from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    # this defines how things are stringified for object. Similar to java
    # if we add a method we dont need to run migration again. Only if we change the structure of the db fsdfsdf sdfsdf sdf sdfsdfsd fsdf sdf sdf sdf sdf sdf sd
    def __str__(self):
        return f"{self.title} - {self.rating} - {self.author}"
