from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProfileForm

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
    
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    http_method_names = ['post', 'get']
    model = Profile
    form_class = ProfileForm
    template_name = 'core/profile_update.html'
        
    def get_success_url(self):
        return reverse_lazy('core:prof_detail', kwargs={'pk': self.object.id})