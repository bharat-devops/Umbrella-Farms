# Generated by Django 3.0.8 on 2020-08-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_app', '0007_auto_20200816_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22_humidity_data',
            name='Date_n_Time',
            field=models.DateTimeField(),
        ),
    ]