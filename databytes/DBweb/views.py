from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    projectList = Project.objects.all()
    jobList = Job.objects.all()
    template = 'index.html'
    context = {'projectList': projectList, 'jobList': jobList}
    return render(request, template, context)

def careers(request):
    projectList = Project.objects.all()
    jobList = Job.objects.all()
    template = 'careers.html'
    context = {'projectList': projectList, 'jobList': jobList}
    return render(request, template, context)