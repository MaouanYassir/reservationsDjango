from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from catalogue.forms.ArtistForm import ArtistForm
from catalogue.models import Artist


# Fonction pour afficher la liste de tous les artistes
def artist_index(request):
    artists = Artist.objects.all()  # récupere les artistes de la base de données
    return render(request, 'artist/index.html', context={'artists': artists})


# fonction pour afficher un artist
def artist_show(request, artist_id):
    try:
        artist = get_object_or_404(Artist, id=artist_id)  # récupere un seul artiste de la BDD
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')

    return render(request, 'artist/show.html', context={'artist': artist})


def edit(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    form = ArtistForm(instance=Artist)
    return render(request, 'artist/edit.html', context={'artist': artist, 'form': form})


def update(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('catalogue:artist-show', artist_id=artist.id)
    return render(request, 'artist/edit.html', {'form': form, 'artist': artist})


def create(request):
    form = ArtistForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue:artist-index')

    return render(request, 'artist/create.html', context={'form': form})
