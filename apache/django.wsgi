import os
import sys

path = '/home/cleveb/git/Games'
if path not in sys.path:
    sys.path.append(path)

path = '/home/cleveb/git/Games/boardgames'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'boardgames.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
