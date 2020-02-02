from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()
    

class Weather(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )

    temp = models.FloatField(default=1)
    wind_speed = models.FloatField(default=None)
    wind_deg = models.FloatField(default=None)
    sky = models.CharField(max_length=15, default=None)
    icon = models.CharField(max_length=10, default=None)
    date = models.DateTimeField(auto_now_add=True)


class HistoryFilter(models.Model):
    name = models.CharField(max_length=30, null=True)
    date_from = models.DateTimeField(null=True)
    date_to = models.DateTimeField(null=True)