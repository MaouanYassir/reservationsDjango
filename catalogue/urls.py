from django.urls import path
from . import views
from .views import PricesListCreateView, ShowListView

app_name = 'catalogue'

urlpatterns = [
    path('artist/', views.artist_index, name='artist-index'),  # route pour afficher tt les articles
    path('artist/<int:artist_id>/', views.artist_show, name='artist-show'),  # route pour afficher un seul artist
    path('artist/edit/<int:artist_id>/', views.artist.edit, name='artist-edit'),  # route pour editer un artist
    path('artist/create/', views.artist.create, name='artist-create'),  # route pour créer un artiste
    path('artist/delete/<int:artist_id>/', views.artist.delete, name='artist-delete'), # route pour supprimer un artiste
    path('api/prices/', PricesListCreateView.as_view(), name='price-list-create'),
    path('api/shows/', ShowListView.as_view(), name='show-list'),
    path('api/prices/<int:show_id>/', views.prices_by_show, name='prices-by-show'),
    # Route pour les tarifs par spectacle
]
