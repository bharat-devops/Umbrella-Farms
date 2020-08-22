from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


########IOT PROJECT#######################################


class DHT22_Temperature_Data(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.DateTimeField()
    Temperature = models.TextField()

    class Meta:
        db_table = "DHT22_Temperature_Data"

    def __str__(self):
        return self.id


class DHT22_Humidity_Data(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.DateTimeField()
    Humidity = models.TextField()

    class Meta:
        db_table = "DHT22_Humidity_Data"

    def __str__(self):
        return self.id


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    class Meta:
        db_table = "Hero"

    def __str__(self):
        return self.name
