from django.contrib import admin
from platforms.models import Platform, Device

admin.site.register(Platform)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['type', 'mac', 'ip', 'platform']

admin.site.register(Device, DeviceAdmin)