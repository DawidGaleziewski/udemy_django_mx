from django import forms
# defines the shape of the form. We just need to extand the clas with form
class ReviewForm(forms.Form):
    # similar to model definition
    user = forms.CharField(max_length=100)