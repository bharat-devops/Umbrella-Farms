# import form class from django
from django.forms import ModelForm
from django import forms

# import GeeksModel from models.py
from .models import Project,Iot_Devices,Device_Details

# create a ModelForm


class ProjectForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Project
		fields = ['proj_name', 'proj_tag', 'proj_lat',
                    'proj_lon', 'proj_zip', 'proj_image', ]


class Iot_DevicesForm(forms.ModelForm):
	# specify the name of model to use
	iot_device = forms.ModelMultipleChoiceField(queryset=Device_Details.objects.values('device_name'))
	iot_project = forms.ModelMultipleChoiceField(
		queryset=Project.objects.values('proj_name'))
	class Meta:
		model = Iot_Devices
		fields = ['iot_device', 'iot_name', 'iot_project',
                    'iot_note', ]
