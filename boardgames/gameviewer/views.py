# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.db.models import Avg
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from decimal import *
from operator import itemgetter
from gameviewer.models import Game, Rating

# helper function
def get_average( game ):
    '''
    Return the average game rating to two decimal places
    '''
    return game.rating_set.all().aggregate(Avg('rating'))

def index(request):
    '''
    Display all the games we currently have
    '''
    latest_game_list = Game.objects.all().order_by('title')
    return render_to_response('gameviewer/index.html', {'latest_game_list':latest_game_list, 'title':'Welcome to my Board Game Collection!'})

def about(request):

    return render_to_response('gameviewer/about.html', {'title':'My board game collection'})

def top(request):
    '''
    display the top 10 rated games
    '''
    # get all the games
    latest_game_list = Game.objects.all()

    top_list = [] 
    for game in latest_game_list:
        # create a list of dictionaries with teh average rating for each game
        top_list.append({'title':game.title, 'id':game.id, 'average_rating':get_average(game)['rating__avg']})

    # sort the games by rating and only take the top 10
    top_list = sorted(top_list, key=itemgetter('average_rating'), reverse=True)[:10] 

    return render_to_response('gameviewer/index.html', {'latest_game_list':top_list, 'title':'Top 10 Rated board games'})

def detail(request, game_id):
    '''
    Display details about the game
    '''

    # get the game object
    g = get_object_or_404(Game, pk=game_id)

    # determine the game average rating
    average = get_average(g)

    return render_to_response('gameviewer/detail.html', {'game': g, 'average_rating': average}, context_instance=RequestContext(request) )

def rate(request, game_id):
    '''
    add a rating to a game
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login( request, user )
            return HttpResonse('successful login')
        else:
            return HttpResonse('disabled account')
    else:
        return HttpResponse('Invalid login')
    '''
    game = get_object_or_404(Game, pk=game_id)
    average = get_average(game)

    try:
        name = request.POST['name']
        rating = request.POST['rating']
        comment = request.POST['comment']
    except (KeyError):
        return render_to_response('gameviewer/detail.html', {'game':game, 'average_rating': average, 'error_message': 'Error - Not all fields are filled in'}, context_instance=RequestContext(request))

    if len(name)== 0:
        return render_to_response('gameviewer/detail.html', {'game':game, 'average_rating':average, 'error_message': 'Error - no name given'}, context_instance=RequestContext(request))

    if len(rating)== 0:
        return render_to_response('gameviewer/detail.html', {'game':game, 'average_rating':average, 'error_message': 'Error - no rating given'}, context_instance=RequestContext(request))
    
    try:
        rating = Decimal(rating)
    except:
        return render_to_response('gameviewer/detail.html', {'game':game, 'average_rating':average,'error_message': 'Error - invalid rating value ' + rating}, context_instance=RequestContext(request))
    
    if rating < 0 or rating > 10:
        return render_to_response('gameviewer/detail.html', {'game':game, 'average_rating':average,'error_message': 'Error - invalid rating value ' + str(rating)}, context_instance=RequestContext(request))

    r = game.rating_set.create(rating=rating, name=name, comment=comment)
    game.save()

    average = get_average(game)

    return render_to_response('gameviewer/detail.html', {'game': game, 'average_rating':average }, context_instance=RequestContext(request) )


def list(request, game_id, search):
    '''
    filter games based on a specific type (search)
    '''

    g = get_object_or_404(Game, pk=game_id)
    
    search_dict = { 'publisher' : 'Games published by ' + g.publisher,
        'genre' : 'Games in the ' + g.genre + ' genre',
        'max' : 'Games that support at least ' + str(g.maxplayers) + ' players', 
        'min' : 'Games that support at least ' + str(g.minplayers) + ' players',
        'year' :'Games published in ' +  g.year_published,
    }

    # TODO - figure out a better way to do this
    if search == 'publisher':
        games = get_list_or_404(Game, publisher=g.publisher)
    elif search == 'genre':
        games = get_list_or_404(Game, genre=g.genre)
    elif search == 'max':
        games = get_list_or_404(Game, maxplayers__gte=g.maxplayers)
    elif search == 'min':
        games = get_list_or_404(Game, minplayers__lte=g.minplayers)
    elif search == 'year':
        games = get_list_or_404(Game, year_published=g.year_published)
    else:
        games = []

    # create the page title
    title = (search_dict.get(search,''))
    
    return render_to_response('gameviewer/index.html', {'latest_game_list': games, 'title':title}) 
