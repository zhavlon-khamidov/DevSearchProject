from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def loginUser(request):
    if(request.user.is_authenticated):
        redirect('projects')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Login or password is incorrect')
            print('Login or password is incorrect')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginUser')