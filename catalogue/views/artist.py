from django.http import Http404
from django.shortcuts import render, get_object_or_404

from catalogue.models import Artist


# Fonction pour afficher la liste de tous les artistes
def artist_index(request):
    artists = Artist.objects.all()  # récupere les artistes de la base de données
    return render(request, 'artist/index.html', context={'artists': artists})


def artist_show(request, artist_id):
    try:
        artist = get_object_or_404(Artist, id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')

    return render(request, 'artist/show.html', context={'artist': artist})
