from django.contrib import admin
from .models import Book, Author, Page


admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'genre')
admin.site.register(Book, BookAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('author', 'book', 'page_number')
admin.site.register(Page, PageAdmin)