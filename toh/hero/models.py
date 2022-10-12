from django.db import models
from traitlets import default


class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=25)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        return f'Hello, my name is Batman and my score is {self.score}!'


class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero, on_delete=models.CASCADE, related_name='leader_set')
    members = models.ManyToManyField(Hero, related_name='teams',)

    def __str__(self):
        return self.name
