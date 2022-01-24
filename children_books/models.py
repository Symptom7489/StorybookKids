from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 50)
    pen_name = models.CharField(max_length=25, unique=True)


    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

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


