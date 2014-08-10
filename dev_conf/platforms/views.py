from django.http import HttpResponse

def index(request):
    return HttpResponse('There will be platforms list')
