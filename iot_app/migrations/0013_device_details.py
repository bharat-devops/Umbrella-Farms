# Generated by Django 3.0.8 on 2020-08-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_app', '0012_project_proj_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device_Details',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=15)),
                ('device_description', models.CharField(max_length=15)),
                ('device_parameters', models.CharField(max_length=15)),
                ('device_code', models.CharField(max_length=15)),
                ('device_image', models.ImageField(blank=True, upload_to='device_upload/')),
            ],
            options={
                'db_table': 'Device_Details',
            },
        ),
    ]
