from rest_framework import viewsets,status
from rest_framework.response import Response
from iot_app import mqtt_serializer
from .models import Hero, DHT22_Humidity_Data, DHT22_Temperature_Data
from .mqtt_serializer import HeroSerializer, DHT22_Humidity_Serializer, DHT22_Temperature_Serializer, TempSerializer




### Temperature Chart Related ###
class TempViewSet(viewsets.ViewSet):
    """test Api Viewset temp """
    #queryset = DHT22_Temperature_Data.objects.all()[:5]
    serializer_class = TempSerializer

    def get(self, request, *args, **kwargs):
        #qs_count = User.objects.all().count()
        self.qs_count1 = DHT22_Temperature_Data.objects.values_list(
            'Temperature').order_by('-id')[:24]
        self.qs_count2 = DHT22_Temperature_Data.objects.values_list(
            'Date_n_Time').order_by('-id')[:24]
        #queryset = DHT22_Temperature_Data.objects.all()
        #serializer = TempSerializer(queryset, many=True)

        #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
        #default_items = [qs_count, 14, 33, 32, 12, 2]
        labels = self.qs_count2
        default_items = self.qs_count1
        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('Temperature'),
            message = f'Hello{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.http_400_bas_request
            )


class DayChartTemp(viewsets.ViewSet):
    """test Api Viewset temp """
    #queryset = DHT22_Temperature_Data.objects.order_by('-id')[:5]
    serializer_class = TempSerializer

    def get(self, request):
        #qs_count = User.objects.all().count()
        qs_count3 = DHT22_Temperature_Data.objects.values_list(
            'Temperature')[:5]
        qs_count4 = DHT22_Temperature_Data.objects.values_list(
            'Date_n_Time')[:5]
        #queryset = DHT22_Temperature_Data.objects.all()
        #serializer = TempSerializer(queryset, many=True)

        #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
        #default_items = [qs_count, 14, 33, 32, 12, 2]
        labels = qs_count4
        default_items = qs_count3
        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('Temperature'),
            message = f'Hello{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.http_400_bad_request
            )


class WeekChartTemp(viewsets.ViewSet):
    """test Api Viewset temp """
    #queryset = DHT22_Temperature_Data.objects.order_by('-id')[:5]
    serializer_class = TempSerializer

    def get(self, request):
        #qs_count = User.objects.all().count()
        weekdefault = DHT22_Temperature_Data.objects.values_list(
            'Temperature')[:10]
        weeklabels = DHT22_Temperature_Data.objects.values_list(
            'Date_n_Time')[:10]
        #queryset = DHT22_Temperature_Data.objects.all()
        #serializer = TempSerializer(queryset, many=True)

        #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
        #default_items = [qs_count, 14, 33, 32, 12, 2]
        labels = weeklabels
        default_items = weekdefault
        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('Temperature'),
            message = f'Hello{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.http_400_bad_request
            )


class MonthChartTemp(viewsets.ViewSet):
    """test Api Viewset temp """
    #queryset = DHT22_Temperature_Data.objects.order_by('-id')[:5]
    serializer_class = TempSerializer

    def get(self, request):
        #qs_count = User.objects.all().count()
        qs_count3 = DHT22_Temperature_Data.objects.values_list(
            'Temperature')[:15]
        qs_count4 = DHT22_Temperature_Data.objects.values_list(
            'Date_n_Time')[:15]
        #queryset = DHT22_Temperature_Data.objects.all()
        #serializer = TempSerializer(queryset, many=True)

        #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
        #default_items = [qs_count, 14, 33, 32, 12, 2]
        labels = qs_count4
        default_items = qs_count3
        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('Temperature'),
            message = f'Hello{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.http_400_bad_request
            )


class YearChartTemp(viewsets.ViewSet):
    """test Api Viewset temp """
    #queryset = DHT22_Temperature_Data.objects.order_by('-id')[:5]
    serializer_class = TempSerializer

    def get(self, request):
        #qs_count = User.objects.all().count()
        qs_count3 = DHT22_Temperature_Data.objects.values_list(
            'Temperature')[:40]
        qs_count4 = DHT22_Temperature_Data.objects.values_list(
            'Date_n_Time')[:40]
        #queryset = DHT22_Temperature_Data.objects.all()
        #serializer = TempSerializer(queryset, many=True)

        #labels = ["Users", "blue", "yellow", "green", "purple", "orange"]
        #default_items = [qs_count, 14, 33, 32, 12, 2]
        labels = qs_count4
        default_items = qs_count3
        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('Temperature'),
            message = f'Hello{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.http_400_bad_request
            )



### Humidity Chart Related ###
### pH Chart Related ###
### EC Chart Related ###
### Water Tank Level Chart Related ###
### Fogger Chart Related ###
### Germination Chart Related ###
### Turbidity Chart Related ###
### Controller Chart Related ###

