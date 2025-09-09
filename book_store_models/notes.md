To make django register models we need to install the app:
```python
INSTALLED_APPS = [
    'book_outlet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

And also use migrations. Migrations define a step for django to touch the database and change it.
This will populate each app "migrations" folder where they are needed
```bash
py .\manage.py makemigrations
```

To apply all migrations that have not been applied yet:
```bash
 py .\manage.py migrate
```

# interactive shell and saving a entry
you can open shell that will have access to your apps by running:
```bash
py .\manage.py shell
```

after that we can do things like play with our models
```python
from book_outlet.models import Book
hp = Book(title="Hary Pyta", rating=2) # creates a new object using model
hp.save() # saves the model to the database
```


# interactive shell and reading the data
you can open shell that will have access to your apps by running:

after that we can do things like play with our models
```python
from book_outlet.models import Book
Book.objects.all() # gets all saved objects
```

# migrations on existing data
if we run migrations, and new data was added, but some data already exists. We will have to choose to eaither provide a one-off default or to add a default in migrations


# updating existing data

To update a entry, we simply need to find a object from models and after that we can update any property and save it.
```python
hp = Book.objects.all()[0]      
hp.author = "JK Rowling"
hp.save()
```
# deleting existing data

```python
hp = Book.objects.all()[0]      
hp.author = "JK Rowling"
hp.delete()
```
