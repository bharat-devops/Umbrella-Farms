# Generated by Django 3.0.8 on 2020-08-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_app', '0005_auto_20200810_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22_temperature_data',
            name='Date_n_Time',
            field=models.TextField(),
        ),
    ]
