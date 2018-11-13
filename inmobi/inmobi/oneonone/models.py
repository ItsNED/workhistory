from django.db import models
from ..devices import models as devices_models
from inmobi.users import models as user_models


class App(devices_models.TimeStampedModel):

    ''' App Model '''

    app_title = models.CharField(max_length=100)
    app_title_eng = models.CharField(max_length=100, blank=True)
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.app_title


class Content(devices_models.TimeStampedModel):

    ''' Content Model '''

    OS_CHOICES = (
        ('ios', 'iOS'),
        ('aos', 'AOS')
    )

    owner = models.ForeignKey(App, on_delete=models.PROTECT, null=True, related_name="content")
    store_url = models.TextField(null=True, blank=True)
    os = models.CharField(max_length=20, choices=OS_CHOICES, null=True)
    events = models.TextField(blank=True)
    adid = models.ForeignKey(devices_models.DeviceAdId, on_delete=models.PROTECT, null=True, blank=True)
    tracking_url = models.TextField(null=True)
    impression_id = models.TextField(blank=True)
    modified_url = models.TextField(blank=True)
    

    def __str__(self):
        return '{} - {}'.format(self.owner.app_title, self.os)


class Result(devices_models.TimeStampedModel):

    ''' Result Model '''

    owner = models.ForeignKey(Content, on_delete=models.PROTECT, null=True, related_name="result")
    result_msg = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.owner.owner.app_title, self.result_msg)

    @property
    def os(self):
        return self.owner.os

    @property
    def impression_id(self):
        return self.owner.impression_id
