from django.conf.urls.defaults import *

urlpatterns = patterns('gameviewer.views',
    (r'^$', 'index'),
    (r'^(?P<game_id>\d+)/$', 'detail'),
)
