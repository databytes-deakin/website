from . import views
from django.urls import path

urlpatterns =  [
    path('', views.index, name='index'),
    path('careers', views.careers, name='careers'),
    path('projects', views.projects, name='projects'),
    path('projects/<project>', views.projectDetails, name='project')
]