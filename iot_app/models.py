from django.db import models
from django.utils import timezone
# Create your models here.


########IOT PROJECT#######################################


class DHT22_Temperature_Data(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Temperature = models.TextField()

    class Meta:
        db_table = "DHT22_Temperature_Data"

    def __str__(self):
        return self.id


class DHT22_Humidity_Data(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Humidity = models.TextField()

    class Meta:
        db_table = "DHT22_Humidity_Data"

    def __str__(self):
        return self.id