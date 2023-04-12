from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def projects(request):
    all_projects = Project.objects.all().order_by('created_date')
    page = 1
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    per_page = 5
    paginator = Paginator(all_projects, per_page)
    page_range = paginator.page_range
    all_projects = paginator.page(page)
    return render(request, 'projects/projects.html',
                  {
                      'projects': all_projects,
                      'page_range':page_range,
                  })

# go to localhost:8000/test-mail to send test mail
def send_test_email(request):
    send_mail(subject='test',
              message='test message',
              from_email='Developer',
              recipient_list=['example@mail.com'])
    return HttpResponse("Email Send")

@login_required
def project(request, pk):
    custom_project = Project.objects.get(id=pk)

    return render(request, 'projects/single-project.html', {'project': custom_project})


@login_required
def create_project(request: HttpRequest):
    form = ProjectForm()
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required
def edit_project(request, pk):
    custom_project = Project.objects.get(id=pk)
    form = ProjectForm(instance=custom_project)
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=custom_project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required
def delete_project(request, pk):
    custom_project = Project.objects.get(id=pk)
    if request.method == 'POST':
        custom_project.delete()
        return redirect('projects')
    context = {'project': custom_project}
    return render(request, 'projects/delete.html', context)
