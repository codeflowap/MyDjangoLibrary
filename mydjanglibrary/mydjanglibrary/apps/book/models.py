from django.db import models
from mydjanglibrary.apps.author.models import Author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    published_at = models.DateField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)