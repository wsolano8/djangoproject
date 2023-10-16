from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


def index(request):
    title = 'Django Course..!!!'
    return render(request, 'index.html', {'titulo':title})

def about(request):
    username = 'wsolano'
    return render(request, 'about.html', {'nombre':username})

def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}</h1>")


def project(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'proyectos':projects})

def task(request):
    #task = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html')