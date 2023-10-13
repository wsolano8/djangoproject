from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("<h1>index Page</h1>")

def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}</h1>")


def about(request):
    return HttpResponse("<h2>Nosotros</h2>")

def project(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"task: {task.tittle}")