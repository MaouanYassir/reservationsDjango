
from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('artist/', views.artist_index, name='artist-index'),  # route pour afficher tt les articles
    path('artist/<int:artist_id>/', views.artist_show, name='artist-show'),  # route pour afficher un seul artist
]