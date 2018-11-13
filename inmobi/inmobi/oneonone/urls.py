from django.urls import path
from inmobi.oneonone.views import (
    ListAllApps,
    )

app_name = "oneonone"

urlpatterns = [
    path('all/', ListAllApps.as_view(), name="all_apps")
]
