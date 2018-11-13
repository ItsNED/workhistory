from rest_framework import serializers
from .models import Device, DeviceAdId


class DeviceAdIdSerializer(serializers.ModelSerializer):

    # device = DeviceSerializer()

    class Meta:
        model = DeviceAdId
        fields = ("adid",)


class DeviceSerializer(serializers.ModelSerializer):

    adids = DeviceAdIdSerializer(many=True)

    class Meta:
        model = Device
        fields = (
            "id",
            "owner",
            "device_name",
            "model_name",
            "os",
            "os_version",
            "phone_number",
            "adids",
        )
