from django.urls import path 
from . import views

app_name = "core"

urlpatterns = [
    path("", views.Homepage.as_view(), name= "home"),
    path("about/", views.About.as_view(), name= "about"),
]
