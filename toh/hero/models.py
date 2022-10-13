from email.policy import default
from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        print(f"Hello, my name is {self.name} and my score is {self.score}")


class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name="leader_set",
    )
    members = models.ManyToManyField(Hero, related_name="teams")
