from django.contrib import admin
from . import models

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title',)

@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('author', 'book', 'page_number')