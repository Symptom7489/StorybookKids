from children_books.models import Page
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
