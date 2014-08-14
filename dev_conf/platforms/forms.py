from django import forms
from platforms.models import Platform, Device
from platforms.models import Platform, Device, CONNECT_TYPE, DEVICE_TYPE

class PlatformForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text=" Name")
    ot_ip = forms.GenericIPAddressField(help_text=" OT ip")
    oxe_ip = forms.GenericIPAddressField(help_text=" OXE ip")
    location = forms.CharField(max_length=128, help_text=" Location")

    class Meta:
        model = Platform


class DeviceForm(forms.ModelForm):
    type = forms.ChoiceField(help_text=" Type", choices=DEVICE_TYPE)
    mac = forms.CharField(max_length=17, help_text=" MAC ")
    ip = forms.GenericIPAddressField(help_text=" IP")
    owner = forms.CharField(max_length=30, help_text="Owner")
    connect_to = forms.ChoiceField(help_text="Connect to", choices=CONNECT_TYPE)
    platform = forms.ModelChoiceField(help_text="Platform", queryset=Platform.objects.all())

    class Meta:
        model = Device


class DeviceTransferForm(forms.Form):
    devices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      label="Transfer this device")


class PlatformTransferForm(forms.ModelForm):
    platform = forms.ModelChoiceField(help_text="Platform", queryset=Platform.objects.all())

    class Meta:
        model = Device
        fields = ['platform']