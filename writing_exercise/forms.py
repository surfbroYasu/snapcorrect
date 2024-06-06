from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import *

class CompositionForm(forms.ModelForm):
    
    class Meta:
        model = Composition
        fields = ['text', 'photo' ]
        
        widgets = {
            "text": forms.Textarea (attrs={"class": "w-full lg:border-l-2 border-orange-500 px-2 py-4", "placeholder": "Write your sentences here!"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ "parent", 'text',]
        widgets = {
            'text': CKEditor5Widget(
                config_name='extends', 
                attrs={"name":"commnet-post"}),
            'parent': forms.TextInput(attrs={"class": "parent-input hidden"}),
        }

# class StatusForm(forms.ModelForm):
#     class Meta:
#         model = Composition
#         fields = ['is_solved']
#         widgets ={
#             'is_solved': forms.BooleanField(attr={'value': 'True'}),
#         }