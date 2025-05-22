from django.shortcuts import render

from workspace.models import Task


def index(request):
    tasks = Task.objects.all().order_by('-datetime')

    context = {
        "tasks": tasks,
    }
    return render(request, "workspace/index.html", context)


