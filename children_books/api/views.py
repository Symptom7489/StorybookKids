from django.shortcuts import render
from children_books.models import Page, Book, Author
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RegistrationSerializer, UserSerializer, BookSerializer, AuthorSerializer, PageSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            author = serializer.save()
            data['response'] = "successfully registered"
            data['email'] = "successfully registered"
            data['username'] = "successfully registered"
        else:
            data = serializer.errors
        return Response(data)



