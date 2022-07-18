from email import message
import re
import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    bloglist = [1,2,3,4,5,6,7,8,9]
    return render(request,'index.html',{'bloglist':bloglist})

# Selected Bolg

def selected_blog(request):
    return render(request,'single-standard.html')

# ---------- Registration -------------

def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Creates Successfully' + user)

    context = {'form' : form}
    return render(request,'registration.html', context)

# ---------- login -------------

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')
    return render(request,'login.html')


# ---------- logout -------------

def logoutuser(request):
    logout(request)
    return render(request, 'login.html')