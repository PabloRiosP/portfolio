from django.shortcuts import render, get_object_or_404
from .models import Project

def renderProjects(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def renderProjectDetail(request, Id):
    project = get_object_or_404(Project, pk=Id)
    return render(request, 'project.html', {'project': project})

def renderTest(request):
    return render(request, 'test.html')

