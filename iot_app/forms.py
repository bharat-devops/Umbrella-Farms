# import form class from django
from django.forms import ModelForm
from django import forms

# import GeeksModel from models.py
from .models import Project

# create a ModelForm


class ProjectForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Project
		fields = ['proj_name', 'proj_tag', 'proj_lat',
                    'proj_lon', 'proj_zip', 'proj_image', ]


