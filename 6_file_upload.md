For uploads to work properly we need to configure folder that will be served from django and what path it will have

```python
MEDIA_ROOT = BASE_DIR / 'media'
# this exposes to the world the media folder
MEDIA_URL = '/media/'
```

next we need to add those settings to urls
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pdf.urls"))
    # manually adding folders that should be exposed to outside word
    # we add media url that we added to settings. Second param is where the files are located on the HDD
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Files should not be stored in a db. However django models, when using file input will have a auto configured way of stopring the file to the hdd (also can be using i.e AWS buckets) and it will just store the ref of that file

```python
from django.db import models

# Create your models here.
class PDF(models.Model):
    name = models.CharField(max_length=100)
    # In general storing file to db is considering a bad practice. So django provides a way to store it to hdd
    # just path is stored in the db
    # where this is stored will depend on settings.py and MEDIA_ROOT directory
    file = models.ImageField(upload_to="pdfs/")
```