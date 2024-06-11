from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import *

# Create your views here.
class Homepage(TemplateView):
    template_name = 'core/home.html'
    pass


class About(TemplateView):
    template_name = 'core/about.html'
    
    
class ProfileDetail(DetailView):
    template_name = 'core/profile_detail.html'
    model = Profile
    context_object_name = 'profile'