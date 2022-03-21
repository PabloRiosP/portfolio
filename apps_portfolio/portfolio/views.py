from django.shortcuts import render, get_object_or_404
from .models import Project, Credential, Hard_Skill, Soft_Skill

def renderHome(request):
    projects = Project.objects.all()
    credentials = Credential.objects.all()
    hard_skills = Hard_Skill.objects.all()
    soft_skills = Soft_Skill.objects.all()
    return render(request, 'home.html', {
        'projects': projects,
        'credentials': credentials,
        'hard_skills': hard_skills,
        'soft_skills': soft_skills
    })

def renderProject(request, Id):
    project = get_object_or_404(Project, pk=Id)
    return render(request, 'project.html', {'project': project})

def renderTest(request):
    return render(request, 'test.html')

