# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello and welcome to my games!")



def detail(request, game_id):
    return HttpResponse("Hello and welcome to the details!" + game_id)
