from rest_framework import serializers
from .models import Device, DeviceAdId

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"


class DeviceAdIdSerializer(serializers.ModelSerializer):

    device = DeviceSerializer()

    class Meta:
        model = DeviceAdId
        fields = "__all__"
