from rest_framework import serializers
from . import models


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = "__all__"


class DeviceAdIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DeviceAdId
        fields = "__all__"
