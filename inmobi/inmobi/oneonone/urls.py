from django.urls import path
from inmobi.oneonone.views import (
    ListAllApps,
    AppListView,
    )

app_name = "oneonone"

urlpatterns = [
    path('all/', ListAllApps.as_view(), name="all_apps"),
    path('view/all/', AppListView.as_view(), name="view_all")
]
