Django has a build in protection against CSRF attacks.
Any post will be checked for it.

In order to pass the protection, we need to add thies field in html forms:

```python
    <form method="post">
        {% csrf_token %}
```

Above will translate to hidden token in a input field.