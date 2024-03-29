# Generated by Django 3.0.8 on 2020-07-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DHT22_Humidity_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SensorID', models.TextField()),
                ('Date_n_Time', models.TextField()),
                ('Humidity', models.TextField()),
            ],
            options={
                'db_table': 'DHT22_Humidity_Data',
            },
        ),
        migrations.CreateModel(
            name='DHT22_Temperature_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SensorID', models.TextField()),
                ('Date_n_Time', models.TextField()),
                ('Temperature', models.TextField()),
            ],
            options={
                'db_table': 'DHT22_Temperature_Data',
            },
        ),
    ]
