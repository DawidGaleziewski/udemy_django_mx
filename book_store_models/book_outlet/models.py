from django.db import models

# Create your models here.
# define data entities here

# () is a way to extand a class in python. We extand class Models this way
class Book(models.Model):
    # all oficialy suported field types: https://docs.djangoproject.com/en/5.2/ref/models/fields/
    # id is created automatically for each entry
    title = models.CharField(max_length=100)
    rating = models.IntegerField()


