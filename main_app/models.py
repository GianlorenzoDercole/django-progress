from django.db import models

# Create your models here.

class Show(models.Model):
    task = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    importance = models.CharField(max_length=50)

    class Rating(models.IntegerChoices):
        GOOD = 1
        BETTER = 2
        FAVORITE = 3
    review = models.IntegerField(choices=Rating.choices)

    def __str__(self):
        return self.title
