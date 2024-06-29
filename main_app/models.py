from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(
        max_length=31
    )

    age = models.PositiveIntegerField()


class Blog(models.Model):
    post = models.TextField()

    author = models.CharField(max_length=35)


class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    precipitation = models.FloatField()
