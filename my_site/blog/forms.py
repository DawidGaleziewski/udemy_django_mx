from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "content": "Your Comment",
            "email": "Your Email"
        }
        # fields = ["user_name", "content", "email"]