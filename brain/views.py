from django.shortcuts import render

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

