from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from workspace.models import Task


def index(request):
    tasks = Task.objects.all().order_by("status", "-datetime")

    context = {
        "tasks": tasks,
    }
    return render(request, "workspace/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("workspace:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("workspace:index")


def switch_status(request, pk: int):
    task = Task.objects.get(pk=pk)
    task.status = not task.status
    task.save()

    return redirect("workspace:index")
