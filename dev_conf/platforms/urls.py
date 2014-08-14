from django.conf.urls import patterns, url
from platforms import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
                           url(r'^about', views.about, name='about'),
                           url(r'^devices', views.devices, name='devices'),
                           url(r'^login', views.user_login, name='login'),
                           url(r'^transfer_devices', views.transfer_devices, name='transfer_devices'),)
