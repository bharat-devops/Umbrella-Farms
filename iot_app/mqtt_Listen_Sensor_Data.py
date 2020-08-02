import django
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'umbrellaFarms.settings'

# Since feeder.py is in Dashboard_app, you need to add the parent directory
# to the python path so that dashex can be imported
# (without this you'll get the 'no module named dashex' error)
#sys.path.append('..')
sys.path.append(os.path.dirname(os.path.abspath('.')))
# Do not forget the change iCrawler part based on your project name


django.setup()
import paho.mqtt.client as mqtt
#from iot_app import store_mqtt_data
from iot_app.store_mqtt_data import sensor_Data_Handler








# MQTT Settings
MQTT_Broker = "192.168.29.103"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/BedRoom/#"

#Subscribe to all Sensors at Base Topic


def on_connect(self,mosq, obj, rc):
	mqttc.subscribe(MQTT_Topic, 0)
	#self.subscribe(MQTT_Topic, 0)

#Save Data into DB Table


def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print("MQTT Data Received...")
	print("MQTT Topic: " + msg.topic)
	#print("Data: " + msg.payload)
	print("message received ", str(msg.payload.decode("utf-8")))
	print("message qos=", msg.qos)
	#print("message retain flag=", msg.retain)
	sensor_Data_Handler(msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass


def on_log(client, userdata, level, buf):
    print("log: ", buf)

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

mqttc.subscribe(MQTT_Topic)
# Continue the network loop
mqttc.loop_forever()
