from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from iot_app import views

router = routers.DefaultRouter()
router.register(r'Heroes', views.HeroViewSet)
router.register(r'DHT22_Temperature', views.DHT22_TemperatureViewSet)
router.register(r'DHT22_Humidity', views.DHT22_HumidityViewSet)
router.register(r'HelloViewSet', views.HelloViewSet,basename='HelloViewSet')
router.register(r'TempViewSet', views.TempViewSet, basename='TempViewSet')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
