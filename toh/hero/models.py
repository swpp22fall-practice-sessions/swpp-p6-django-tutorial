from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name