# Generated by Django 3.0.6 on 2020-08-01 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0008_auto_20200730_1114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DHT22_Humidity_Data',
        ),
        migrations.DeleteModel(
            name='DHT22_Temperature_Data',
        ),
    ]