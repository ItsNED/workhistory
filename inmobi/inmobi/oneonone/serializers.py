from rest_framework import serializers
from . import models

class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.App
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Result
        fields = '__all__'
