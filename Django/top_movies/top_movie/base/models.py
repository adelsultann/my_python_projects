from django.db import models

# Create your models here.



class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=False)
    description = models.CharField(max_length=500)
    rating = models.FloatField()
    link = models.CharField(max_length=200)


    def __str__(self):
        return self.title

