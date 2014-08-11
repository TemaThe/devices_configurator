from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from platforms.models import Platform, Device

def index(request):
    context = RequestContext(request)
    platform_list = Platform.objects.order_by('-name')[:5]
    context_dict = {'platforms': platform_list}
    return render_to_response('platforms/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Info about app platforms"}
    return render_to_response('platforms/about.html', context_dict, context)

def devices(request):
    context = RequestContext(request)
    devices_list = Device.objects.order_by('-type')[:5]
    context_dict = {'devices': devices_list}
    return render_to_response('platforms/devices.html', context_dict, context)