from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from os.path import exists, join, isdir

from .brain import doc_list, doc_redirect, list_files, page_settings, render_doc


# Display the document that matches the URL
class DocView(TemplateView):
    template_name = 'doc.html'

    def get(self, request, *args, **kwargs):
        doc = self.kwargs.get('title')
        while doc.endswith('/'):
            doc = doc[:-1]
        url = doc_redirect(doc)
        if url:
            return HttpResponseRedirect(url)
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        doc = self.kwargs.get('title')
        path = join('Documents', doc)
        text = render_doc(doc)
        return page_settings(title=path, text=text)


# Display the list of document files in a directory
class FilesView(TemplateView):
    template_name = 'files.html'

    def get_context_data(self, **kwargs):
        title = self.kwargs.get('title')
        path = join('Documents', title)
        if exists(path) and isdir(path):
            files = list_files(title)
            return page_settings(title=title, files=files)


# Display the documents in a directory by title
class IndexView(TemplateView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        title = self.kwargs.get('title')
        doc = self.request.path[1:]
        path = join('Documents', title)
        if exists(path) and isdir(path):
            docs = doc_list(title)
            text = render_doc(doc)
            return page_settings(title=title, docs=docs, text=text)


# Display the document that matches the URL
class MissingView(TemplateView):
    template_name = 'missing.html'

    def get_context_data(self, **kwargs):
        title = 'Missing Document'
        doc = self.kwargs.get('title')
        path = join('Documents', doc)
        return page_settings(title=title, doc=doc, path=path)


# Forward from / to /seamanfamily/brain/Index
class RedirectRoot(RedirectView):
    url = '/seamanfamily/brain/'



