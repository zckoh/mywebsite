from django.shortcuts import render
from projects.models import Project
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def projects_index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
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
