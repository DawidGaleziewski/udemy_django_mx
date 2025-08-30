# urls are matched with views in URL view

```python
urlpatterns = [
    path("", views.index),
    # django will attempt to convert value to int. And if not possible it will go to next request
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challange")
]
```

# views can be named and accssed in views via reverse
```python
path("<str:month>", views.monthly_challenge, name="month-challange")
```

# reverse is a safe way of creating dynamic routes in our views i.e for links and is a recomand way of doing things
```python
redirect_path = reverse("month-challange", args=[month_name])
```

# Django allows us to declare same path with diffrent types
``` python
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challange")
```
