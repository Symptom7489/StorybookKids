from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)
    pen_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=30)


class Page(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_image = models.ImageField()
    page_number = models.IntegerField()
