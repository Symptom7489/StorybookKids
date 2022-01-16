from children_books.models import Page
from rest_framework import serializers
from django.contrib.auth.models import User

class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['img_upload', 'page_number']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']
