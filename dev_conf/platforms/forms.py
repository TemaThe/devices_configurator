from django import forms
from platforms.models import Platform, Device


class PlatformForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter platform name")
    ot_ip = forms.GenericIPAddressField(help_text="Enter OT ip")
    oxe_ip = forms.GenericIPAddressField(help_text="Enter OXE ip")

    class Meta:
        model = Platform


class DeviceForm(forms.ModelForm):
    type = forms.CharField(max_length=17, help_text="Enter Type")
    mac = forms.CharField(max_length=17, help_text="Enter mac")
    ip = forms.GenericIPAddressField(help_text="Enter IP")
    platform = forms.ModelChoiceField(queryset=Platform.objects.all())

    class Meta:
        model = Device
