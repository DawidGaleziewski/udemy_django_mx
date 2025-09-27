from django.db import models

# Create your models here.
class PDF(models.Model):
    name = models.CharField(max_length=100)
    # In general storing file to db is considering a bad practice. So django provides a way to store it to hdd
    # just path is stored in the db
    # where this is stored will depend on settings.py and MEDIA_ROOT directory
    file = models.ImageField(upload_to="pdfs/")
