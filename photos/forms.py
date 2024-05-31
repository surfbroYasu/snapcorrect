from django import forms
from .models import *


class PhotographerRegist(forms.ModelForm):
    
    class Meta:
        model = Photographer
        fields = ['bio', 'base_location', 'image', 'artist_name' ]
        
        widgets = {
            'artist_name': forms.TextInput(attrs={"placeholder": "活動名または氏名"}),
            'base_location': forms.TextInput(attrs={"placeholder": "活動エリア"}),
            'bio': forms.Textarea(attrs={"class": "w-full lg:border-l-2 border-orange-500 px-2 py-4", "wrap": "hard", "cols": 80, "rows": 4, "placeholder": "自己紹介など"}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

class PhotoUploadForm(forms.ModelForm):
    
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description', 'category']
        
        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "タイトル"}),
            'description': forms.Textarea(attrs={"class": "w-full lg:border-l-2 border-orange-500 px-2 py-4", "wrap": "hard", "cols": 80, "rows": 4, "placeholder": "説明文"}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
