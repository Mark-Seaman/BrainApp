# settings.py   - Build the smallest possible web app

from django.conf.urls import url
from django.http import HttpResponse

# Required Django Setup
DEBUG=True
SECRET_KEY = 'KDqYibgo1ZI4QIHOFInXmTy6wknXxWiii5DBal825FQgCXo5zA'
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'hammer.settings'
ALLOWED_HOSTS = ['*']

# Home View
def home(request):
    title = "World's Simplest App"
    text = '''
    Digital Ocean creates a blank Django app which is replaced by this code.
    This is the simplest Django app that is possible. All extra stuff has
    been stripped out. Only essential code remains. Source code lives
    in <b>~/hammer/simple.py</b>.
    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))

# URL Route
urlpatterns = [
    url(r'^$', home),
]
