from django.forms import ModelForm
from .models import Book, Page

class PageModelForm(ModelForm):
    class Meta:
        model = Page
        fields = ('book', 'page_image', 'page_number', 'author')
