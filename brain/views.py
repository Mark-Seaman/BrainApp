from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now
from os.path import exists, join, isdir

from .brain import  doc_list, doc_redirect, render_doc

# # Display the document that matches the URL
# class BrainView(TemplateView):
#     template_name = 'doc.html'
#
#     def get_context_data(self, **kwargs):
#         doc = self.request.path[1:]
#         path = join('Documents', doc)
#         text = render_doc(doc)
#         header = dict(title='Brain', subtitle='Document View')
#         return dict(header=header, title=path, text=text, time=now())
#
#     def get(self, request, *args, **kwargs):
#         doc = self.request.path[1:]
#         while doc.endswith('/'):
#             doc = doc[:-1]
#         url = doc_redirect(doc)
#         if url:
#             return HttpResponseRedirect(url)
#         return self.render_to_response(self.get_context_data(**kwargs))


def page_settings(**kwargs):
    path = kwargs.get('path')
    header = dict(title='My Notes', subtitle=path)
    settings = dict(header=header, title=path, time=now())
    settings.update(kwargs)
    return settings


# Display the document that matches the URL
class DocView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        doc = self.request.path[1:]
        path = join('Documents', doc)
        text = render_doc(doc)
        # header = dict(title='My Notes', subtitle=path)
        # return dict(header=header, title=path, text=text, time=now())
        return page_settings(path=path, text=text)

    def get(self, request, *args, **kwargs):
        doc = self.request.path[1:]
        while doc.endswith('/'):
            doc = doc[:-1]
        url = doc_redirect(doc)
        if url:
            return HttpResponseRedirect(url)
        return self.render_to_response(self.get_context_data(**kwargs))


# Display the document that matches the URL
class IndexView(DocView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        title = self.kwargs.get('title')
        doc = self.request.path[1:]
        path = join('Documents', title)
        if exists(path) and isdir(path):
            docs = doc_list(title)
            text = render_doc(doc)
            # header = dict(title='My Notes', subtitle=path)
            # return dict(header=header, title=doc, docs=docs, text=text, time=now())
            return page_settings(path=path, docs=docs, text=text)



# Display the document that matches the URL
class MissingView(TemplateView):
    template_name = 'missing.html'

    def get_context_data(self, **kwargs):
        path = join('Documents', self.kwargs.get('title'))
        text = 'Missing Document'
        # title = 'Missing Document'
        # header = dict(title='My Notes', subtitle=path)
        # return dict(header=header, title=title, path=path, time=now())
        return page_settings(path=path, text=text)


# Forward from / to /seamanfamily/brain/Index
class RedirectRoot(RedirectView):
    url = '/seamanfamily/brain/'



