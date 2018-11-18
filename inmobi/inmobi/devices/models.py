from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Device(TimeStampedModel):

    ''' Device Model '''

    OS_CHOICES = (
        ('ios', 'iOS'),
        ('aos', 'AOS')
    )

    owner = models.CharField(max_length=100)
    device_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=200, blank=True)
    os = models.CharField(max_length=30, choices=OS_CHOICES)
    os_version = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{}의 {}'.format(self.owner, self.device_name)


class DeviceAdId(TimeStampedModel):

    ''' DeviceAdId Model '''

    device = models.ForeignKey(Device, on_delete=models.PROTECT, null=True, related_name="adids")
    adid = models.CharField(max_length=50, null=False)

    def __str__(self):
        return '{}의 {}'.format(self.device.owner, self.device.device_name)




