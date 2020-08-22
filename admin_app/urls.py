from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'admin_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    # path('login', views.login, name='login'),
    # path('tables', views.tables, name='tables'),
    # path('cards', views.cards, name='cards'),
    # path('flot', views.flot, name='flot'),
    # path('morris', views.morris, name='morris'),
    # path('forms', views.forms, name='forms'),
    # path('panels_wells', views.panels_wells, name='panels_wells'),
    # path('buttons', views.buttons, name='buttons'),
    # path('notifications', views.notifications, name='notifications'),
    # path('typography', views.typography, name='typography'),
    # path('icons', views.icons, name='icons'),
    # path('grid', views.grid, name='grid'),
    # path('blank', views.blank, name='blank'),
    # path('login', views.login, name='login'),
#
    path('html404', views.html404, name='html404'),
    path('blank', views.blank, name='blank'),
    path('buttons', views.buttons, name='buttons'),
    path('cards', views.cards, name='cards'),
    path('charts', views.charts, name='charts'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('index', views.index, name='index'),
 
    path('register', views.register, name='register'),
    path('tables', views.tables, name='tables'),
    path('utilities_animation', views.utilities_animation, name='utilities_animation'),
    path('utilities_border', views.utilities_border, name='utilities_border'),
    path('utilities_color', views.utilities_color, name='utilities_color'),
    path('utilities_other', views.utilities_other, name='utilities_other'),
    path('Project', views.add_project, name='Project'),
    path('Iot', views.add_iot, name='Iot'),


]
