# Umbrella-Farms
IOT solutions for the Polyhouse

MQTT Server needs to be installed on either windows or linux server wherever the django deployed. 
Once the Mqtt server or Broker is installed , Django can take control of it.

For windows/linux installation Software::

https://mosquitto.org/download/

If you are not interested in installing the software , there is always https://test.mosquitto.org/ to test your mqtt client code .


When adding Device ,
After Submit button , It should display the code to be attached to that sensor to send data to the topic .
These details should be saved to a cloumn.

so that it can be checked back.

A listener for that topic will be opneded up

When we delete the sensor , it should delete topic listener as well 
Listeners are written in paho-mqtt client
mqtt broker is local to where django is deployed 



