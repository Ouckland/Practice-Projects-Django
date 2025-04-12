from django.shortcuts import render, redirect, get_object_or_404
from .models import Artist, Genre
from .forms import ArtistForm
from django.contrib import messages
# Create your views here.

def home(request):
    context = {
    }
    return render(request, 'pages/home.html')

def display_artists(request):
    artists = Artist.objects.all()
    context = {
        "artists": artists
    }
    return render(request, "pages/display.html", context)


def add_artist(request):
    form = ArtistForm()

    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, "Artist Succesfully Added")
            return redirect('music_engine:display_artists')
    context = {
        "form": form,
    }
    return render(request, "pages/add-artist.html", context)



def delete_artist(request, id):
    try:
        artist = get_object_or_404(Artist, id=id)
        if request.method == "POST":
            artist.delete()
            messages.success(request, "Succesfully Deleted Artist")
            return redirect('music_engine:display_artists')
        return render(request, 'pages/delete-artist.html', {"artist": artist})
    except Artist.DoesNotExist:
        return render(request, 'pages/404.html', context={"error": "Artist does not exist"})
    except Exception as e:
        return render(request, 'pages/505.html', context={f"error": str(e)})
        
def update_artist(request, id):
    try:
        artist = get_object_or_404(Artist, id=id)
        form = ArtistForm(instance=artist)

        if request.method =='POST':
            form = ArtistForm(request.POST, instance=artist)
            if form.is_valid:
                form.save()
                messages.success(request, "Succesfully Updated")
                return redirect('music_engine:display_artists')
        context = {
            "form": form,
            "artist": artist,
                   }
        return render(request, 'pages/update-artist.html', context)
    except Artist.DoesNotExist:
        return render(request, 'pages/404.html', context={"error": "Artist does not exist"})        