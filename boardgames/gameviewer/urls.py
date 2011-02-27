from django.conf.urls.defaults import *

urlpatterns = patterns('gameviewer.views',
    (r'^$', 'index'),
    (r'^(?P<game_id>\d+)/$', 'detail'),
    (r'^list/(?P<game_id>\d+)/(?P<search>\w+)/$', 'list'),
)
