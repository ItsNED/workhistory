from rest_framework.views import APIView
from rest_framework.response import Response
from inmobi.oneonone import models, serializers


class ListAllApps(APIView):

    def get(self, request, format=None):
        
        all_apps = models.App.objects.all()

        serializer = serializers.AppSerializer(all_apps, many=True)

        return Response(data=serializer.data)