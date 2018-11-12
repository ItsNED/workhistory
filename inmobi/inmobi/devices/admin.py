from django.contrib import admin
from .models import Device, DeviceAdId

@admin.register(Device)
class devicesAdmin(admin.ModelAdmin):
    list_display = ('owner', 'device_name', 'phone_number')


@admin.register(DeviceAdId)
class deviceAdIdAdmin(admin.ModelAdmin):
    list_display = ('device', 'adid')
