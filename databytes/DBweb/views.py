from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    projectList = Project.objects.all()
    jobList = Job.objects.all()
    testimonyList = Testimony.objects.all()
    template = 'index.html'
    context = {'projectList': projectList, 'jobList': jobList, 'testimonyList': testimonyList}
    return render(request, template, context)

def careers(request):
    jobList = Job.objects.all()
    template = 'careers.html'
    context = {'jobList': jobList}
    return render(request, template, context)

def projects(request):
    projectList = Project.objects.all()
    template = 'projects.html'
    context = {'projectList': projectList}
    return render(request, template, context)

def project(request):
    project = Project.objects.all()
    template = 'project-details.html'
    context = {'project': project}
    return render(request, template, context)

def projectDetails(request):
    projectDetails = Project.objects.all()
    template = 'project-details.html'
    context = {'project': projectDetails}
    return render(request, template, context)
