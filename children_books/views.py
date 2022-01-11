from django.shortcuts import render
from django.views.generic import ListView
from .models import Page

class PageListView(ListView):

    model = Page
    template_name = 'index.html'
    pass


