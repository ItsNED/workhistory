from django.urls import path
from . import views

app_name = "oneonone"

urlpatterns = [
    path('', views.test, name="test")
]
