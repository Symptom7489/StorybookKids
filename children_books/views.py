from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Page
from .forms import PageModelForm

class PageListView(ListView):

    model = Page
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = 'Ryan'
        return context

class PageFormView(CreateView):
    template_name = 'page-form.html'
    model = Page
    form_class = PageModelForm
    success_url = 'success.html'