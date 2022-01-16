from django.shortcuts import render
from children_books.models import Page
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PageSerializer, UserSerializer
from django.contrib.auth.models import User

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes =[permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]