from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from platforms.models import Platform, Device
from platforms.forms import PlatformForm, DeviceForm


def check_form(form):
    if form.is_valid():
        form.save(commit=True)
    else:
        print form.errors

def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PlatformForm(request.POST)
        check_form(form)

    form = PlatformForm()
    platform_list = Platform.objects.order_by('-name')[:5]
    context_dict = {'form': form, 'platforms': platform_list}

    return render_to_response('platforms/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Info about app platforms"}
    return render_to_response('platforms/about.html', context_dict, context)

def devices(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        check_form(form)

    form = DeviceForm()

    devices_list = Device.objects.order_by('-type')[:5]
    context_dict = {'form': form, 'devices': devices_list}
    return render_to_response('platforms/devices.html', context_dict, context)