from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now
from os.path import join

from .brain import document_html, list_files


class RedirectPage(RedirectView):
    url = '/seamanfamily/brain/'

    def get_redirect_url(self, *args, **kwargs):
        path = join('/', self.request.path[1:], 'Index')



# Display the document that matches the URL
class FolderView(TemplateView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        title = 'Folder View'
        path = self.kwargs.get('title', 'Index')
        files = list_files(path)
        header = dict(title='Brain App Demo', subtitle='Folder View')
        return dict(header=header, title=title, files=files, time=now())


# Display the document that matches the URL
class DocView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        title = 'Brain App Demo'
        path = self.kwargs.get('title', 'Index')
        text = document_html(path)
        header = dict(title='Brain App Demo', subtitle='Document View')
        return dict(header=header, title=title, text=text, time=now())

    # def get(self, request, *args, **kwargs):
    #     url = doc_page(self.request.path[1:])
    #     if url:
    #         log('REDIRECT: %s --> %s' % (title, url))
    #         return HttpResponseRedirect('/%s/' % url)
    #
    #     return self.render_to_response(self.get_context_data(**kwargs))
