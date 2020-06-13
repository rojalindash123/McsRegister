from django.shortcuts import render,redirect
from django.contrib import messages
from django import forms
from django.contrib.auth import login, authenticate
# from .forms import UserCreationForm
from django.contrib.auth.models import User,auth
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import get_user_model
# User = get_user_model()

def welcome(request):
    return render(request,'welcome.html')


def register(request):
# if request.method == 'POST':
#         first_name=request.POST['first_name']
#         last_name = request.POST['last_name']
#         mobile=request.POST['mobile']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,mobile=mobile)
#         user.save()
#         return redirect('/login_user/')
# else:
#    return render(request,'register.html')
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login_user/')
    else:
        form=CreateUserForm()
    return render(request,'signup.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        # username = User.objects.get(email=email).username
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credential')
            return redirect('/login_user/')

    else:
        return render(request,'login.html');

def logout(request):
    auth.logout(request)
    return redirect('/')