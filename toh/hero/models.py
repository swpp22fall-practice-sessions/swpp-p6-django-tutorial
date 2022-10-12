from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        print("Hello, my name is %s and my score is %d!" %(self.name, self.score))


class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='leader_of')
    members = models.ManyToManyField(Hero, related_name='member_of')

    def __str__(self):
        return self.name