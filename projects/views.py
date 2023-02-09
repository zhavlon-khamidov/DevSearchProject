from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

""" allProjects =[
    {"id" : 1, "title" : "First project", 'description' : 'This is my first project'},
    {"id" : 2, "title" : "Second project", 'description' : 'This is my first project'},
    {"id" : 3, "title" : "Third project", 'description' : 'This is my first project'},
    {"id" : 4, "title" : "Fourth project", 'description' : 'This is my first project'},
] """

def projects(request):
    allProjects = Project.objects.all()
    return render(request,'projects/projects.html',
        {'projects' : allProjects})

def project(request, pk):
    project = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-project.html',{'project': project})