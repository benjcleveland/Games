from gameviewer.models import Game 
from django.contrib import admin

class GameAdmin( admin.ModelAdmin ):
    list_display = ('title', 'publisher', 'last_played' )

admin.site.register(Game, GameAdmin)
