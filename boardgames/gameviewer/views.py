# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from gameviewer.models import Game

def index(request):
    latest_game_list = Game.objects.all().order_by('title')
    return render_to_response('gameviewer/index.html', {'latest_game_list':latest_game_list, 'title':'Welcome to my Board Game Collection!'})


def detail(request, game_id):
    g = get_object_or_404(Game, pk=game_id)
    return render_to_response('gameviewer/detail.html', {'game': g})


def list(request, game_id, search):
    '''
    filter games based on a specific type (search)
    '''

    g = get_object_or_404(Game, pk=game_id)
    
    search_dict = { 'publisher' : g.publisher,
        'genre' : g.genre,
    }

    if search == 'publisher':
        games = get_list_or_404(Game, publisher=g.publisher)
    elif search == 'genre':
        games = get_list_or_404(Game, genre=g.genre)
    else:
        games = []

    # create the page title
    title = 'Games with a ' + search + ' matching "' + search_dict.get(search,'') + '"'
    
    return render_to_response('gameviewer/index.html', {'latest_game_list': games, 'title':title}) 
