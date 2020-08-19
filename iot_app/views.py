from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework import permissions
from .mqtt_serializer import HeroSerializer, DHT22_Humidity_Serializer, DHT22_Temperature_Serializer, TempSerializer
from .models import Hero,DHT22_Humidity_Data,DHT22_Temperature_Data
from iot_app import mqtt_serializer
# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()

class HeroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class DHT22_TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DHT22_Temperature_Data.objects.all()
    serializer_class = DHT22_Temperature_Serializer
    #permission_classes = [permissions.IsAuthenticated]
    # def get(self,request,format=None):
    #     data = DHT22_Temperature_Data.Temperature

    #     return Response(data)
    # def get(self, request, format=None):
    #     data = {
    #         "sales": 100,
    #         "customers": 10,
    #         "Users": User.objects.all().count()
    #     }
    #     return Response(data)



class DHT22_HumidityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DHT22_Humidity_Data.objects.all()
    serializer_class = DHT22_Humidity_Serializer
    #permission_classes = [permissions.IsAuthenticated]


class HelloViewSet(viewsets.ViewSet):
    """test Api Viewset """
    serializer_class = HeroSerializer
    def get(self,request):
        qs_count = User.objects.all().count()
        labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
        default_items = [qs_count,14,33,32,12,2]
        #labels = DHT22_Temperature_Data.Date_n_Time
        #default_items = DHT22_Temperature_Data.Temperature
        data = {
            'labels': labels,
            'default': default_items,

        }
        return Response(data)
    def create(self,request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name'),
            message = f'Hello{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.http_400_bas_request
            )

    


    def put (self,request,format=None):
        labels = ["red","blue","yellow","green","purple","orange"]
        data = {
            "labels": labels,
            "default": 10,
            "users": User.objects.all().count(),

        }
        return Response(data)


# class TempViewSet(viewsets.ViewSet):
#     """test Api Viewset temp """
#     #queryset = DHT22_Temperature_Data.objects.all()[:5]
#     serializer_class = TempSerializer

#     def get(self, request, *args, **kwargs):
#         #qs_count = User.objects.all().count()
#         self.qs_count1 = DHT22_Temperature_Data.objects.values_list('Temperature').order_by('-id')[:24]
#         self.qs_count2 = DHT22_Temperature_Data.objects.values_list(
#             'Date_n_Time').order_by('-id')[:24]
#         #queryset = DHT22_Temperature_Data.objects.all()
#         #serializer = TempSerializer(queryset, many=True)
        
#         #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
#         #default_items = [qs_count, 14, 33, 32, 12, 2]
#         labels = self.qs_count2
#         default_items = self.qs_count1
#         data = {
#             'labels': labels,
#             'default': default_items,
#         }
#         return Response(data)

#     def create(self, request):
#         """Create a New hello message"""
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data.get('Temperature'),
#             message = f'Hello{name}!'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.http_400_bas_request
#             )


# class DayChartTemp(viewsets.ViewSet):
#     """test Api Viewset temp """
#     #queryset = DHT22_Temperature_Data.objects.order_by('-id')[:5]
#     serializer_class = TempSerializer

#     def get(self, request):
#         #qs_count = User.objects.all().count()
#         qs_count3 = DHT22_Temperature_Data.objects.values_list(
#             'Temperature')[:5]
#         qs_count4 = DHT22_Temperature_Data.objects.values_list(
#             'Date_n_Time')[:5]
#         #queryset = DHT22_Temperature_Data.objects.all()
#         #serializer = TempSerializer(queryset, many=True)

#         #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
#         #default_items = [qs_count, 14, 33, 32, 12, 2]
#         labels = qs_count4
#         default_items = qs_count3
#         data = {
#             'labels': labels,
#             'default': default_items,
#         }
#         return Response(data)
    

#     def create(self, request):
#         """Create a New hello message"""
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data.get('Temperature'),
#             message = f'Hello{name}!'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.http_400_bad_request
#             )




