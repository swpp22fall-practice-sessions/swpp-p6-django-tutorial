from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)