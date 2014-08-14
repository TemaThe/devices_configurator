from django.db import models

CONNECT_TYPE = (('OT', 'OT'), ('OXE', 'OXE'),)
DEVICE_TYPE = (('VHE', 'VHE'), ('IPTOUCH', 'IPTOUCH'), ('VLE', 'VLE'),)

class Platform(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ot_ip = models.GenericIPAddressField()
    oxe_ip = models.GenericIPAddressField()
    location = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Device(models.Model):
    type = models.CharField(max_length=10, choices=DEVICE_TYPE)
    mac = models.CharField(max_length=17, unique=True)
    ip = models.GenericIPAddressField(unpack_ipv4=False, unique=True)
    owner = models.CharField(max_length=128)
    connect_to = models.CharField(max_length=3, choices=CONNECT_TYPE)
    platform = models.ForeignKey(Platform)

    def __unicode__(self):
        return self.mac