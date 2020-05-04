from django.contrib.auth.models import User
from django.db import models

CHOICES_GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    gender = models.CharField(choices=CHOICES_GENDER, max_length=16)
    birth_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
