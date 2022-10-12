from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)

    def introduce(self):
        print("Hello, my name is " + self.name + " and my score is " + str(self.score))

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set'
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams'
    )

    def __str__(self):
        return self.name
