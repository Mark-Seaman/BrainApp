from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now
from os.path import exists, join, isdir

from .brain import document_html, doc_list, doc_redirect, list_files, render_doc


class RedirectRoot(RedirectView):
    url = '/seamanfamily/brain/'


class RedirectIndex(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return join(self.request.path[:-1], 'Index')


# Display the document that matches the URL
class FolderView(TemplateView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        doc = self.request.path[1:]
        path = join('Documents', doc)
        if exists(path) and isdir(path):
            # files = list_files(doc)
            docs = doc_list(doc)
            header = dict(title='Brain', subtitle='Folder View')
            return dict(header=header, title=doc, docs=docs, time=now())


# Display the document that matches the URL
class IndexView(TemplateView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        title = self.kwargs.get('title')
        doc = self.request.path[1:]
        if doc.endswith('/'):
            doc = doc[:-1]
        path = join('Documents', title)
        if exists(path) and isdir(path):
            docs = doc_list(title)
            text = render_doc(doc)
            header = dict(title='Brain', subtitle='Index View')
            return dict(header=header, title=doc, docs=docs, text=text, time=now())


# Display the document that matches the URL
class DocView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        doc = self.request.path[1:]
        # path = join('Documents', doc)
        # if not exists(path) and exists(path+'.md'):
        #     doc = doc+'.md'
        # text = document_html(doc)
        path = join('Documents', doc)
        text = render_doc(doc)
        header = dict(title='Brain', subtitle='Document View')
        return dict(header=header, title=path, text=text, time=now())

    def get(self, request, *args, **kwargs):
        doc = self.request.path[1:]
        url = doc_redirect(doc)
        if url:
            return HttpResponseRedirect(url)
        return self.render_to_response(self.get_context_data(**kwargs))


