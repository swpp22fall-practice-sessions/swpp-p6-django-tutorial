from email.policy import default
from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        print('Hello, my name is {} and my score is {}'.format(
            self.name, self.score))
