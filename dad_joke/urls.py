from django.urls import path
from . import views


app_name = "dad_joke"

urlpatterns = [
    path('', views.joke_view, name='joke'),
    path('add-favorite/<str:joke_id>/', views.AddFavoriteJoke.as_view(), name='add_favorite'),
]
