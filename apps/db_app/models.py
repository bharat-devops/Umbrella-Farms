from django.db import models
# Create your models here.

import json
from django.db import models
from django.utils import timezone

########SCRAPPY PROJECT#######################################
class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField()  # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id

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
