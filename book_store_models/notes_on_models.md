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

# create vs save
We can create an object and hit database with it instantly
```python
 Book.objects.create(title="DBZ", rating=1, author="Kojima")
``` 

# get a value from DB by values

We can a value by values provided. I.E.
However this will throw a error if there are multiple values returned
```python
Book.objects.get(title="DBZ", author="Kojima")
```

If we want multiple entires. We can use filter
```python
Book.objects.filter(title="DBZ")

## filtering lower then or equal. Django supplied value. Those are called "modifiers"
 Book.objects.filter(rating__lte=2, title__contains="harry")
```


# more advance queryies using Q

a tool called Q is provided by django to build more advanced queries

```python
from django.db.models import Q

Book.objects.filter(Q(rating__lt=5) | Q(author="Kojima"))

# this will return a query definition. But will NOT touch the database yet.
query_1 = Book.objects.filter(Q(rating__lt=5) | Q(author="Kojima"))

## this howaver WILL run the actual query. And it will ALSO cache the result. Therefore next time we run this it won't just hit the db again
print(query_1)

# this will re-use the results that were cached. It will not hit the db again
print(query_1)

# this is worth remembering. Because if we do something like this. Database will be hit twice:
Book.objects.filter(Q(rating__lt=5) | Q(author="Kojima"))
Book.objects.filter(Q(rating__lt=5) | Q(author="Kojima"))
```


# Models relations

```python
# creates new table in db for authors
class Author(models.Model):
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
```

# quering a table that has relations with other table
```python
## __ joins related table
Book.objects.filter(author__last_name="Rawling")
```

# inverse relations
```python
## this is how we can access books that were written by this authour, despite it not having a field for book
author = Author.objects.all()[0]
author.book_set.get()
```

# connecting models

We first need to create a table to relete it to another. Otherwise we will get a error
```python
px = Address(street="Phenix", city="London", state="Weessex", zipcode="12345")
px.save()

jk.address = px
 jk.save()
```