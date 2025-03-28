from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import context
from django.urls import reverse

from users.forms import UserLoginForm

def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context ={
        'title':'Регистрация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context ={
        'title':'Регистрация',
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context ={
        'title':'Личный кабинет',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...