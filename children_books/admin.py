from django.contrib import admin
from .models import Book, Author, Page

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'pen_name')
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'genre')
admin.site.register(Book, BookAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('author', 'book', 'page_number')
admin.site.register(Page, PageAdmin)