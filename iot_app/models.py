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


class Project(models.Model):
    proj_name = models.CharField(max_length=15, primary_key=True, unique=True)
    proj_tag = models.CharField(max_length=15, blank=True)
    proj_lat = models.FloatField(('Latitude'), blank=True, null=True)
    proj_lon = models.FloatField(('Longitude'), blank=True, null=True)
    proj_zip = models.CharField(max_length=60)
    proj_created = models.DateTimeField(auto_now=True)
    proj_last_updated = models.DateTimeField(auto_now=True)
    proj_image = models.ImageField(upload_to='image_upload/', blank=True)

    class Meta:
        db_table = "Project"

    def __str__(self):
        return self.proj_name

class User_Details(models.Model):   
    user_first_name = models.CharField(max_length=15)
    user_last_name = models.CharField(max_length=15)
    user_email = models.CharField(max_length=15)
    user_address = models.CharField(max_length=15)
    user_city = models.CharField(max_length=15)
    user_state = models.CharField(max_length=15)
    user_zip = models.CharField(max_length=15)
    user_phone = models.CharField(max_length=15)

    class Meta:
        db_table = "User_Details"

    def __str__(self):
        return self.user_first_name


class Device_Details(models.Model):
    device_name = models.CharField(max_length=15, primary_key=True)
    device_description = models.TextField()
    device_parameters = models.TextField()
    device_code = models.CharField(max_length=15)
    device_tech_details = models.TextField(blank=True)
    device_image = models.ImageField(upload_to='device_upload/', blank=True)
    class Meta:
        db_table = "Device_Details"

    def __str__(self):
        return self.device_name


class Iot_Devices(models.Model):
    iot_device = models.CharField(max_length=25, primary_key=True)
    iot_name = models.CharField(max_length=25,unique=True)
    iot_project = models.CharField(max_length=25)
    iot_note = models.TextField(blank=True)

    class Meta:
        db_table = "Iot_Devices"

    def __str__(self):
        return self.iot_name


