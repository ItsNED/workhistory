from django.urls import path
from inmobi.devices.views import (
    ListAllDevices,
    ListAllDeviceAdIds,
    )

app_name = "devices"

urlpatterns = [
    path("all/", ListAllDevices.as_view(), name="list_devices"),
    path("adids/", ListAllDeviceAdIds.as_view(), name="list_devices"),
]
