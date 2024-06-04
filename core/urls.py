from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


app_name = "core"

urlpatterns = [
    path("", views.Homepage.as_view(), name= "home"),
    path("about/", views.About.as_view(), name= "about"),

    re_path(r'^google0e9665c9287f6795\.html$', TemplateView.as_view(template_name="google0e9665c9287f6795.html", content_type='text/html')),
]
