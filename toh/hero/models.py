from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def introduce(self):
        return f'Hello, my name is {self.name} and my score is {self.score}!'