from django.urls import path

from workspace.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,

)

app_name = "workspace"

urlpatterns = [
    path("", index, name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
]