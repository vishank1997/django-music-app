from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

"""def index(request):
    all_albums = Album.objects.all()
    #html = ''
    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #    html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))
"""


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums,}
    return render(request, "music/index.html", context)


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
        context = {"album": album}
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")
    return render(request, "music/detail.html", context)


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select an album",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, "music/detail.html", {'album':album})

