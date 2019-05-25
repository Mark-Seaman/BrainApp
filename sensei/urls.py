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
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^newpage$', home),
]

