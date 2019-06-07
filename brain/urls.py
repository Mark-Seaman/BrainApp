from django.conf.urls import url

from .views import DocView, FolderView, IndexView, RedirectIndex, RedirectRoot


# URL Routes
urlpatterns = [

    url(r'^$',                              RedirectRoot.as_view()),
    url(r'^(?P<title>[\w/\-.]*)/Index$',    IndexView.as_view()),
    url(r'^(?P<title>[\w/\-.]*)/$',         RedirectIndex.as_view()),
    url(r'^(?P<title>[\w/\-.]*)$',          DocView.as_view()),
]

# url(r'^(?P<title>[\w/.]*)/$',           FolderView.as_view()),

# from django.conf import settings
    # from django.conf.urls.static import static
    # from django.contrib import admin

    #    url(r'^admin/', admin.site.urls),
    # url(r'^brain/Index$',               BrainView.as_view()),
    # url(r'^markdown$',                  MarkdownView.as_view()),
    # url(r'^brain/redirect$',            RedirectPage.as_view()),


# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
