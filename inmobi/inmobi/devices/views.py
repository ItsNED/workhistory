from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllDevices(APIView):

    def get(self, request, format=None):
        
        all_devices = models.Device.objects.all()

        serializer = serializers.DeviceSerializer(all_devices, many=True)

        return Response(data=serializer.data)

class ListAllDeviceAdIds(APIView):

    def get(self, request, format=None):

        all_devices_adids = models.DeviceAdId.objects.all()

        serializer = serializers.DeviceAdIdSerializer(all_devices_adids, many=True)

        return Response(data=serializer.data)