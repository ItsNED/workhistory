from rest_framework.views import APIView
from rest_framework.response import Response
from inmobi.oneonone import models, serializers
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView


class ListAllApps(APIView):

    def get(self, request, format=None):
        
        all_apps = models.App.objects.all()

        serializer = serializers.AppSerializer(all_apps, many=True)

        return Response(data=serializer.data)


class AppListView(ListView):

    model = models.App

    def get_queryset(self):
        qs = models.App.objects.all()
        print(qs)
        return qs
    
