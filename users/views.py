from django.shortcuts import render, redirect
from .forms import EmailedUserCreationForm
from django.http import HttpResponse, request
from django.urls import reverse
from django.contrib.auth import login


def index(request):
    
    return render(request=request,template_name='users/index.html')

def register(request):
    if request.method == 'POST':
        form = EmailedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('users:index'))
        else:
            return redirect(reverse('register'))
    else:
        form = EmailedUserCreationForm()
        return render(request=request,template_name='users/register.html',context={'form':form})

