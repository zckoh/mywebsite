from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projects_index(request):
    project = Project.objects.all()
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    projects = Project.objects.all()
    context = {
        'project': project,
        'projects': projects
    }
    return render(request, 'projects/project_detail.html', context)
