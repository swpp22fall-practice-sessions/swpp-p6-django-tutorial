from email.policy import default
from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def introduce(self):
        print(f'Hello, my name is {self.name} and my score is {self.score}')
    
class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete = models.CASCADE, #If leader is gone, the team is deleted
        related_name='leader_set', #hero.leader_set returns QuerySet<Team> that contains team whose leader is hero
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )
    
    def __str__(self):
        return self.name