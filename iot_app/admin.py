from django.contrib import admin
from .models import DHT22_Temperature_Data,DHT22_Humidity_Data,Hero
# Register your models here.

admin.site.register(DHT22_Humidity_Data)
admin.site.register(DHT22_Temperature_Data)
admin.site.register(Hero)
