from django import forms

class UploadForm(forms.Form):
    name = forms.CharField(max_length=100)
    file = forms.ImageField(allow_empty_file=False)