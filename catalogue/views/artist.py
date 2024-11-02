from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from catalogue.forms.ArtistForm import ArtistForm
from catalogue.models import Artist
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


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

@login_required
def edit(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    form = ArtistForm(request.POST or None, instance=artist)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Artiste modifié avec succès.")
            return redirect('catalogue:artist-show', artist_id=artist.id)
        else:
            messages.error(request, "Échec de la modification de l'artiste!")
    return render(request, 'artist/edit.html', {'form': form, 'artist': artist})


def create(request):
    form = ArtistForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Nouvel artiste créé avec succès.")
            return redirect('catalogue:artist-index')

        else:
            messages.add_message(request, messages.ERROR, "Échec de l'ajout d'un nouvel artiste !")

    return render(request, 'artist/create.html', context={'form': form})


@login_required
@permission_required('catalog.can_delete', raise_exception=True)
def delete(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        artist.delete()
        messages.success(request, "Artiste supprimé avec succès.")

        return redirect('catalogue:artist-index')

    else:
        messages.error(request, "Échec de la suppression de l'artiste !")

    # Si la méthode n'est pas POST, rediriger vers la page de l'artiste
    return render(request, 'catalogue/artist/show.html', {
        'artist': artist,
    })
