from django.urls import path

from workspace.views import (
    index,
)

app_name = "workspace"

urlpatterns = [
    path("", index, name="index"),
]