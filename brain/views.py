from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now
from os import listdir

from brain.brain import document_html


class RedirectPage(RedirectView):
    url = '/seamanfamily/brain/'


# Display the document that matches the URL
class FolderView(TemplateView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        title = 'Folder View'
        # path = self.kwargs.get('title', 'Index')
        path = 'seamanfamily/brain'
        files = listdir('Documents/'+path)
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



