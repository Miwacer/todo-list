from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from workspace.models import Task, Tag


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


class SwitchTaskStatusView(View):
    def post(self, request, pk: int, *args, **kwargs):
        task = Task.objects.get(pk=pk)
        task.status = not task.status
        task.save()

        return redirect("workspace:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("workspace:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("workspace:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("workspace:tag-list")
