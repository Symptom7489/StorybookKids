from django.shortcuts import render
from django.views.generic import ListView
from .models import Page

class PageListView(ListView):

    model = Page
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = 'Ryan'
        return context

