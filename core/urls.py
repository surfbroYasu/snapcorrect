from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


app_name = "core"

urlpatterns = [
    path("", views.Homepage.as_view(), name= "home"),
    path("about/", views.About.as_view(), name= "about"),
]
