from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Here is the platforms."}
    return render_to_response('platforms/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Info about app platforms"}
    return render_to_response('platforms/about.html', context_dict, context)