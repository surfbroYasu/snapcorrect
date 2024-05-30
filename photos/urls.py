from django.urls import path 
from . import views

app_name = "photos"

urlpatterns = [
    path("", views.GalleryView.as_view(), name= "gallery"),
    path("photographer/<int:pk>/", views.PhotographerDetail.as_view(), name="photographer"),
    path("create-photographer/", views.PhotographerCreate.as_view(), name="create_photographer"),
    path("update-photographer/<int:pk>/", views.PhotographerUpdate.as_view(), name="edit_photographer"),
]
