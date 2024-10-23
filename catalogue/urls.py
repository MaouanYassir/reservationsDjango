from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('artist/', views.artist_index, name='artist-index'),  # route pour afficher tt les articles
    path('artist/<int:artist_id>/', views.artist_show, name='artist-show'),  # route pour afficher un seul artist
    path('artist/edit/<int:artist_id>/', views.artist.edit, name='artist-edit'),  # route pour editer un artist
    path('artist/update/<int:artist_id>/', views.artist.update, name='artist-update'),  # route pour modifier un artist
    path('artist/create/', views.artist.create, name='artist-create'),  # route pour créer un artiste
    path('artist/delete/<int:artist_id>/', views.artist.delete, name='artist-delete')  # route pour supprimer un artiste
]
