from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    return HttpResponse("<h1>List of all projects</h1>")

def project(request, pk):
    return HttpResponse(f"<h1>Project with id: {pk}</h1>")