from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

allProjects =[
    {"id" : 1, "title" : "First project", 'description' : 'This is my first project'},
    {"id" : 2, "title" : "Second project", 'description' : 'This is my first project'},
    {"id" : 3, "title" : "Third project", 'description' : 'This is my first project'},
    {"id" : 4, "title" : "Fourth project", 'description' : 'This is my first project'},
]

def projects(request):
    page = 'All Projects'
    number = 10
    return render(request,'projects/projects.html',
        {'page' : page, 'num' : number, 'projects' : allProjects})

def project(request, pk):
    page = 'Single Project'
    sProject = None
    for p in allProjects:
        print('p -> ',p)
        print('id: ',p['id'],pk)
        if p['id'] == int(pk):
            sProject = p
            break
    print(sProject)
    return render(request, 'projects/single-project.html',{'page' : page, 'project': sProject})