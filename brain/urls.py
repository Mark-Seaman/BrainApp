from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

# Home View
def home(request):
    title = "Brain Page"
    text = '''
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/brain/">Brain</a></li>
        <li><a href="index">Index</a></li>
    </ul>

    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))

# Index View
def index(request):
    title = "Brain Index Page"
    text = '''
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/brain/">Brain</a></li>
        <li><a href="index">Index</a></li>
    </ul>
    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))
 

# URL Routes 
urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^index$', index),
]
