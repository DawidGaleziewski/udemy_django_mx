from django import forms
from .models import Review
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


# Abstraction for creating forms basing on existing model
class ReviewForm2(forms.ModelForm):
    # we let know django with which model this class is related
    class Meta:
        model = Review
        # we specify which fields we want to show in the form. we can also set this to __all__
        fields = ['name' ,"review", "rating"]
        # We can also override labels etc
        labels = {
            "name": "Your Name :)",
            "review": "Your Review :)",
            "rating": "Your Rating :)"
        }
        error_messages = {
            "name": {
                "required": "You can't be empty. DUH!",
            }
        }