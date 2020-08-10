from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Hero,DHT22_Temperature_Data,DHT22_Humidity_Data


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')


class DHT22_Temperature_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DHT22_Temperature_Data
        fields = ['id', 'SensorID', 'Date_n_Time', 'Temperature']


class DHT22_Humidity_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DHT22_Humidity_Data
        fields = ['id', 'SensorID', 'Date_n_Time', 'Humidity']


class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DHT22_Temperature_Data
        fields = ('Date_n_Time','Temperature')
