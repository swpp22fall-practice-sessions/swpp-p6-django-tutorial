from email.policy import default
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=25)
    
    def __str__(self) -> str:
        return self.name