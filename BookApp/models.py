from django.db.models import Model
from django.db import models
import jsonfield

# Create your models here.


class Book(Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publishedDate = models.CharField(max_length=50)
    industryIdentifiers = jsonfield.JSONField()
    pageCount = models.IntegerField()
    imageLinks = jsonfield.JSONField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title
