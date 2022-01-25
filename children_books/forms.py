from django.forms import ModelForm
from .models import Page
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class PageModelForm(ModelForm):
    class Meta:
        model = Page
        fields = ('book', 'page_image', 'page_number', 'author')


