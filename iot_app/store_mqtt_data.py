
#from . import mqtt_Listen_Sensor_Data
from django.conf import settings
import sqlite3
from django.utils import timezone
from iot_app.models import DHT22_Humidity_Data, DHT22_Temperature_Data
import django,os,json
print("store mqtt data")




def DHT22_Humidity_Data_Handler(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Date_and_Time = json_Dict['Date']
	Humidity = json_Dict['Humidity']
	#DHT22_Humidity_Data = DHT22_Humidity_Data()
	insert_value = DHT22_Humidity_Data(SensorID = SensorID, Date_n_Time = Date_and_Time, Humidity = Humidity )
	insert_value.save()


def DHT22_Temperature_Data_Handler(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Date_and_Time = json_Dict['Date']
	Temperature = json_Dict['Temperature']
	#DHT22_Temperature_Data = DHT22_Temperature_Data()
	insert_value = DHT22_Temperature_Data(SensorID = SensorID, Date_n_Time = Date_and_Time, Temperature = Temperature )
	insert_value.save()


def sensor_Data_Handler(Topic, jsonData):
	if Topic == "Home/BedRoom/DHT22/Temperature":
		DHT22_Temperature_Data_Handler(jsonData)
	elif Topic == "Home/BedRoom/DHT22/Humidity":
		DHT22_Humidity_Data_Handler(jsonData)
