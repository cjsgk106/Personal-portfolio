from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, project_id):
    detailproject = get_object_or_404(Job, pk=project_id)
    return render(request, 'jobs/detail.html', {'detailproject':detailproject})
