"""databytes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from DBweb import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('careers', views.careers, name='careers'),
    path('projects', views.projects, name='projects'),
    path('projects/<str:ProjectURL>', views.project, name='project'),
    path('careers/<str:JobURL>', views.career, name='career'),
    path('admin', admin.site.urls)
]
