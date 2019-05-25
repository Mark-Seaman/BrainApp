"""sensei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


# Home View
def home(request):
    title = "Home Page"
    text = '''
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="index">Index</a></li>
    </ul>

    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))

# Index View
def index(request):
    title = "Index Page"
    text = '''
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="index">Index</a></li>
    </ul>
    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))
 
# URL Route
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^index$', index),
]

