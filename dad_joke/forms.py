from django import forms
from .models import JokeComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = JokeComment
        fields = ["content"]
