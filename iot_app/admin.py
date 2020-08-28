from django.contrib import admin
from .models import DHT22_Temperature_Data,DHT22_Humidity_Data,Hero,Project,User_Details,Device_Details,Iot_Devices
#from iot_app.models import *
# Register your models here.

admin.site.register(DHT22_Humidity_Data)
admin.site.register(DHT22_Temperature_Data)
admin.site.register(Hero)
admin.site.register(Project)
admin.site.register(User_Details)
admin.site.register(Device_Details)
admin.site.register(Iot_Devices)
 

