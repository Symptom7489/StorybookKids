from children_books.models import Page, Author, Book
from rest_framework import serializers
from django.contrib.auth.models import User

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['page_image', 'page_number', 'author', 'book']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pen_name', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'genre', 'description']
