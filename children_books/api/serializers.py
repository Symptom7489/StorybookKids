from children_books.models import Page, Author, Book
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['page_image', 'page_number', 'author', 'book']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


            # password = validated_data.pop('password')
            # user = User(**validated_data)
            # user.set_password(password)


            # user = User(
            #     is_superuser=validated_data['username']
            # )
            # user.set_password(validated_data['password'])


            # user.save()
            # return user

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author

        fields = ['id', 'pen_name', 'first_name', 'last_name', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'genre', 'description']

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['email', 'first_name', 'last_name', 'pen_name']

    def save(self):
        author = Author(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            pen_name=self.validated_data['pen_name'],
        )