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
		widgets = {
		    'title': forms.TextInput(
				attrs={
				    'class': 'form-control'
				}
		    ),
		    'content': forms.Textarea(
				attrs={
				    'class': 'form-control'
				}
		    ),
		}


class Iot_DevicesForm(forms.ModelForm):
	# specify the name of model to use
	#iot_device = forms.ModelMultipleChoiceField(queryset=Device_Details.objects.values('device_name'))
	iot_device = forms.ModelMultipleChoiceField(
		queryset=Device_Details.objects.values_list('device_name',flat=True).distinct())
	#using('sensors').values_list('value', flat=True)
	iot_project = forms.ModelMultipleChoiceField(
		queryset=Project.objects.values_list('proj_name',flat=True).distinct())
	class Meta:
		model = Iot_Devices
		fields = ['iot_device', 'iot_name', 'iot_project',
				    'iot_note', ]
