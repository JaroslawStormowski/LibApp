from django.db.models import Model
from django.db import models
import jsonfield
import uuid

# Create your models here.


class Book(Model):
    id_uuid = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=100, blank=True, null=True)
    publishedDate = models.CharField(max_length=50, blank=True, null=True)
    industryIdentifiers = jsonfield.JSONField(blank=True, null=True)
    pageCount = models.IntegerField(blank=True, null=True)
    imageLinks = jsonfield.JSONField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
