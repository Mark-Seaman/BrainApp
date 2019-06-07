from django.conf.urls import url

from .views import DocView, FilesView, IndexView, MissingView, RedirectRoot


# URL Routes
urlpatterns = [
    url(r'^$',                              RedirectRoot.as_view()),
    url(r'^(?P<title>[\w/\-.]*)/Files$',    FilesView.as_view()),
    url(r'^(?P<title>[\w/\-.]*)/Index$',    IndexView.as_view()),
    url(r'^(?P<title>[\w/\-.]*)/Missing$',  MissingView.as_view()),
    url(r'^(?P<title>[\w/\-.]*)$',          DocView.as_view()),
]
