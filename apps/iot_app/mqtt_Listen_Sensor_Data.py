import paho.mqtt.client as mqtt
import sys
print('\n'.join(sys.path))
from store_mqtt_data import sensor_Data_Handler




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
