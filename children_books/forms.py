from django.forms import ModelForm
from .models import Book, Page

class PageModelForm(ModelForm):
    class Meta:
        model = Page
        fields = ('book', 'img_upload', 'page_number', 'author')
