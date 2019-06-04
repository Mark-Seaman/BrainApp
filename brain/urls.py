from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

from .views import BrainView, HomeView, IndexView


# URL Routes 
urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^index$', IndexView.as_view()),
    url(r'^brain$', BrainView.as_view()),
]
