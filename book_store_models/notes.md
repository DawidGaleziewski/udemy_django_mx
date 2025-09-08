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
