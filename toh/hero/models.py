from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=120, null=False)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    def introduce(self):
        return 'Hello, my name is {} and my score is {}!'.format(self.name, self.score)


class Team(models.Model):
    name = models.CharField(max_length=120, null=False)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set',
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )

    def __str__(self):
        return self.name