from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from iot_app import views
from iot_app import charts_view
from rest_framework.schemas import get_schema_view
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
#router1 = routers.DefaultRouter()
router.register(r'Heroes', views.HeroViewSet)
router.register(r'DHT22_Temperature', views.DHT22_TemperatureViewSet)
router.register(r'DHT22_Humidity', views.DHT22_HumidityViewSet)
router.register(r'HelloViewSet', views.HelloViewSet,basename='HelloViewSet')
router.register(r'TempViewSet', charts_view.TempViewSet, basename='TempViewSet')
router.register(r'DayChartTemp', charts_view.DayChartTemp, basename='DayChartTemp')
router.register(r'WeekChartTemp', charts_view.WeekChartTemp, basename='WeekChartTemp')
router.register(r'MonthChartTemp', charts_view.MonthChartTemp, basename='MonthChartTemp')
router.register(r'YearChartTemp', charts_view.YearChartTemp,
                basename='YearChartTemp')

schema_view = get_schema_view(title='Temperature API',
                              description='An API to read Temperature Data')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('/api/', include(router.urls)),
    path('/schema/', schema_view),
    path('/docs/', include_docs_urls(title='Temperature API')),
    # path('api1/', include(router1.urls)),
    path('/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
