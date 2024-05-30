from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Homepage(TemplateView):
    template_name = 'core/home.html'
    pass


class About(TemplateView):
    template_name = 'core/about.html'
    