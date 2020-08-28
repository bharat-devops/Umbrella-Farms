from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from iot_app.forms import ProjectForm,Iot_DevicesForm


@login_required(login_url='/login/')
def index(request):
    return render(request, 'admin_app/index.html')


@login_required(login_url='/login/')
def tables(request):
    return render(request, 'admin_app/tables.html')


@login_required(login_url='/login/')
def cards(request):
    return render(request, 'admin_app/cards.html')
    
def flot(request):
    return render(request, 'admin_app/flot.html')


def morris(request):
    return render(request, 'admin_app/morris.html')


def forms(request):
    return render(request, 'admin_app/forms.html')


def panels_wells(request):
    return render(request, 'admin_app/panels_wells.html')


def buttons(request):
    return render(request, 'admin_app/buttons.html')


def notifications(request):
    return render(request, 'admin_app/notifications.html')


def typography(request):
    return render(request, 'admin_app/typography.html')


def icons(request):
    return render(request, 'admin_app/icons.html')


def grid(request):
    return render(request, 'admin_app/grid.html')


@login_required(login_url='/login/')
def blank(request):
    return render(request, 'admin_app/blank.html')


# def login(request):
#     return render(request, 'admin_app/login.html')


def html404(request): 
   return render(request, 'admin_app/html404.html')


@login_required(login_url='/login/')
def base(request): 
    return render(request, 'admin_app/base.html')
@login_required(login_url='/login/')
def charts(request): 
    return render(request, 'admin_app/charts.html')

def forgot_password(request): 
    return render(request, 'admin_app/forgot_password.html')
@login_required(login_url='/login/')
def index_old(request): 
    return render(request, 'admin_app/index_old.html')

def register(request): 
    return render(request, 'admin_app/register.html')


@login_required(login_url='/login/')
def tables_static(request): 
    return render(request, 'admin_app/tables_static.html')
@login_required(login_url='/login/')
def utilities_animation(request): 
    return render(request, 'admin_app/utilities_animation.html')


@login_required(login_url='/login/')
def utilities_border(request): 
    return render(request, 'admin_app/utilities_border.html')


@login_required(login_url='/login/')
def utilities_color(request): 
    return render(request, 'admin_app/utilities_color.html')


@login_required(login_url='/login/')
def utilities_other(request): 
    return render(request, 'admin_app/utilities_other.html')


# @login_required(login_url='/login/')
# def add_project(request):
#     return render(request, 'admin_app/Project.html')

@login_required(login_url='/login/')
def add_iot(request):
    form = Iot_DevicesForm(request.POST or None)
    return render(request, 'admin_app/Iot.html', {'form': form})


def project_view(request):
    form = ProjectForm(request.POST or None)
    return render(request, 'admin_app/Project.html', {'form': form})


# def add_iot(request):
#     form = Iot_DevicesForm(request.POST or None)
#     return render(request, 'admin_app/Iot.html', {'form': form})



