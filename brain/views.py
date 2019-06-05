from django.shortcuts import render
from subprocess import Popen, PIPE
from sys import version_info

# Create your views here.
from django.views.generic import RedirectView, TemplateView
from django.utils.timezone import now


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

markdown = '''# Markdown Text Format
## Cheatsheet for formats

Paragraph

* Bullet list
* List item

1. Numbered list
1. List item

'''
class MarkdownView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        title = 'Markdown View'
        text = markdown_to_html(markdown)
        return dict(title=title, text=text)
    
    
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
