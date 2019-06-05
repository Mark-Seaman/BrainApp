from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now
from os import listdir

from brain.brain import document_html


# class HomeView(TemplateView):
#     template_name = 'home.html'


# class IndexView(TemplateView):
#     template_name = 'index.html'


class RedirectPage(RedirectView):
    url = '/seamanfamily/brain/'


# class BrainView(TemplateView):
#     template_name = 'brain_theme.html'
#
#     def get_context_data(self, **kwargs):
#         title = self.kwargs.get('title', 'Index')
#         header = dict(title='Brain App Demo', subtitle='Brain Page Template')
#         text = '''
#             This page shows how to configure a view by using a template.
#             The template contains variables (such as title and text) that
#             are passed to the template from the view code.  The result is
#             a view that contains dynamic data.
#             '''
#         return dict(title=title, text="no text", header=header, time=now())
#

# Display the document that matches the URL
class FolderView(TemplateView):
    template_name = 'folder.html'

    def get_context_data(self, **kwargs):
        title = 'Folder View'
        # path = self.kwargs.get('title', 'Index')
        path = 'seamanfamily/brain'
        files = listdir('Documents/'+path)
        return dict(title=title, files=files)


# Display the document that matches the URL
class DocView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        title = 'Brain App Demo'
        path = self.kwargs.get('title', 'Index')
        text = document_html(path)
        header = dict(title='Brain App Demo', subtitle='Document View')
        return dict(header=header, title=title, text=text)


# # View to display markdown text
# class MarkdownView(TemplateView):
#     template_name = 'markdown.html'
#
#     def get_context_data(self, **kwargs):
#         title = 'Markdown View'
#         path = 'seamanfamily/brain/Markdown.md'
#         text = document_html(path)
#         return dict(title=title, text=text)
#



