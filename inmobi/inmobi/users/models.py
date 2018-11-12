from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):

    TEAM_CHOICES = (
        ('pso', 'PSO'),
        ('game', 'GAME'),
        ('ops', 'OPS'),
        ('brand', 'BRAND'),
        ('bd', 'BD'),
        ('not-specified', 'Not Specified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    phone = models.CharField(max_length=20, null=True)
    team = models.CharField(max_length=80, null=True, choices=TEAM_CHOICES)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
