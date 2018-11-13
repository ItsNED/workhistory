from rest_framework import serializers
from . import models

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Result
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):

    result = ResultSerializer(many=True)

    class Meta:
        model = models.Content
        fields = (
            'id',
            'owner',
            'store_url',
            'os',
            'events',
            'adid',
            'tracking_url',
            'impression_id',
            'modified_url',
            'result',
        )


class AppSerializer(serializers.ModelSerializer):

    content = ContentSerializer(many=True)

    class Meta:
        model = models.App
        fields = (
            'id',
            'app_title',
            'app_title_eng',
            'content',
            'creator',
        )