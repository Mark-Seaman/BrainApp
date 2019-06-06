from django.conf.urls import url
from django.contrib import admin

from .views import  DocView, FolderView, RedirectRoot


# URL Routes 
urlpatterns = [
#    url(r'^admin/', admin.site.urls),

    url(r'^$',                          RedirectRoot.as_view()),

    # url(r'^index$',                     IndexView.as_view()),

    # url(r'^brain/redirect$',            RedirectPage.as_view()),

    url(r'^(?P<title>[\w/.]*)/$',       FolderView.as_view()),

    url(r'^(?P<title>[\w/.]*)$',        DocView.as_view()),

    # url(r'^brain/Index$',               BrainView.as_view()),

    # url(r'^markdown$',                  MarkdownView.as_view()),
]
