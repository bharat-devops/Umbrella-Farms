# Generated by Django 3.0.8 on 2020-07-30 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0006_dht22_humidity_data_dht22_temperature_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dht22_humidity_data',
            old_name='SensorID',
            new_name='SensorID1',
        ),
        migrations.RenameField(
            model_name='dht22_temperature_data',
            old_name='SensorID',
            new_name='SensorID1',
        ),
    ]