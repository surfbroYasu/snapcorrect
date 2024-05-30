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
        fields = ["commenting_to", "parent", 'text',]
        widgets = {
            'text': CKEditor5Widget(
                config_name='extends', 
                attrs={"name":"commnet-post"}),
            # 'commenting_to': forms.HiddenInput(),
            # 'parent': forms.HiddenInput(),
            
            'commenting_to': forms.TextInput(attrs={"class": "hidden"}),
            'parent': forms.TextInput(attrs={"class": "hidden"}),
        }
