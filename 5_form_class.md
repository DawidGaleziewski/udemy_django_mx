Django provides us a 'forms class' which we can use to create form object in a easy way that will allow us to valiudate the input data. But also to use it as HTML form.

By convention we create a 'forms.py' file for this purpose.

```python
from django import forms
# defines the shape of the form. We just need to extand the clas with form
class ReviewForm(forms.Form):
    # similar to model definition
    # form field is also vonfuurable by its params
    user = forms.CharField(max_length=20, label="Your Name",
       error_messages={
           "required": "Can't be empty. DUH!",
           "max_length": "That is way to long BRO!"

    })
    review = forms.CharField(widget=forms.Textarea, min_length=6, max_length=200, label="Your Review")
    rating = forms.IntegerField(min_value=1, max_value=5, label="Your Rating")
```