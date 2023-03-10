from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def projects(request):
    allProjects = Project.objects.all()
    return render(request,'projects/projects.html',
        {'projects' : allProjects})

@login_required
def project(request, pk):
    project = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-project.html',{'project': project})

@login_required
def createProject(request : HttpRequest):
    form = ProjectForm()
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    
    context = {'form':form}
    return render(request,'projects/project-form.html', context)

@login_required
def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    
    context = {'form':form}
    return render(request,'projects/project-form.html', context)

@login_required
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'project':project}
    return render(request, 'projects/delete.html',context)