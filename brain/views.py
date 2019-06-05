from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now
from subprocess import Popen, PIPE
from sys import version_info


class HomeView(TemplateView):
    template_name = 'home.html'

class IndexView(TemplateView):
    template_name = 'index.html'


class BrainView(TemplateView):
    template_name = 'brain_theme.html'

    def get_context_data(self, **kwargs):
        title = self.kwargs.get('title', 'Index')
        header = dict(title='Brain App Demo', subtitle='Brain Page Template')
        return dict(title=title, text="no text", header=header, time=now())


class MarkdownView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        title = 'Markdown View'
        markdown = read_markdown('seamanfamily/brain/Markdown.md')
        text = markdown_to_html(markdown)
        return dict(title=title, text=text)

    
def read_markdown(doc):
    return open('Documents/%s' % doc).read()
   
    
def markdown_to_html(markdown):
    return shell_pipe('pandoc', markdown)


def shell_pipe(command, stdin=''):
    p = Popen(command, stdin=PIPE, stdout=PIPE)
    if version_info.major == 3:
        (out, error) = p.communicate(input=stdin.encode('utf-8'))
        if error:
            return error.decode('utf-8') + out.decode('utf-8')
        return out.decode('utf-8')
    else:
        (out, error) = p.communicate(input=stdin)
        if error:
            return "**stderr**\n" + error + out
        return out
