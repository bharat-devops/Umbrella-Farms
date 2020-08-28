# Generated by Django 3.0.8 on 2020-08-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_app', '0017_auto_20200827_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iot_Devices',
            fields=[
                ('iot_device', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('iot_name', models.CharField(max_length=25, unique=True)),
                ('iot_project', models.CharField(max_length=25)),
                ('iot_note', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Iot_Devices',
            },
        ),
        migrations.RemoveField(
            model_name='device_details',
            name='device_id',
        ),
        migrations.AlterField(
            model_name='device_details',
            name='device_name',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
