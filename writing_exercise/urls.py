from django.urls import path 
from . import views

app_name = "writing"

urlpatterns = [
    path("select-image/", views.PhotoList.as_view(), name="photo_list"),
    
    path("<int:pk>/compose", views.CompositionCreate.as_view(), name="writing_page"),
    path("<int:pk>/delete", views.DeleteComposition.as_view(), name="delete_composition"),
    
    # class room is the page for comments and replies of a composition
    path('class-room/<int:pk>', views.ClassRoom.as_view(), name="class_room"),
    
    
    
    
    path("waiting-list/", views.WaitingList.as_view(), name="waiting_list"),
    path('my-collection/', views.MyCollection.as_view(), name='collection'),
    
    path("comment-like/<int:pk>", views.CommentUpdate.as_view(), name="like"),
    
]
