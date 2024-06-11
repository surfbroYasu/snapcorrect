from django import forms
from .models import Profile, School

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["birthday", 'image', 'is_teacher']
