from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ot_ip = models.GenericIPAddressField(name='OT', unpack_ipv4=False)
    oxe_ip = models.GenericIPAddressField(name='OXE', unpack_ipv4=False)

    def __unicode__(self):
        return self.name

class Device(models.Model):
    type = models.CharField(max_length=128, unique=True)
    mac = models.CharField(max_length=17)
    ip = models.GenericIPAddressField(unpack_ipv4=False)
    platform = models.ForeignKey(Platform)

    def __unicode__(self):
        return self.mac