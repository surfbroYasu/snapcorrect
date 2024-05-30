from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# FORMS
from .forms import *

# Models
from .models import Photo, Photographer


class GalleryView(ListView):
    template_name =  "photos/gallery.html"
    model = Photo


class PhotographerDetail(DetailView):
    template_name = "photos/photographer.html"
    model = Photographer
    context_object_name = "photographer"
    
class PhotographerCreate(LoginRequiredMixin, CreateView):
    template_name = "photos/photographer_create.html"
    model = Photographer
    context_object_name = "photographer"
    form_class = PhotographerRegist
    
    def form_valid(self, form):
        print("****CALLLLLLLL")
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('photos:photographer', kwargs={'pk': self.object.id})
    
    
  
class PhotographerUpdate(LoginRequiredMixin, UpdateView):
    template_name = "photos/photographer_update.html"
    model = Photographer
    form_class = PhotographerRegist
    
    
    def get_success_url(self):
        return reverse_lazy('photos:photographer', kwargs={'pk': self.object.id})