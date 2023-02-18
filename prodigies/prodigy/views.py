from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangoLogin
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    context = {
        
    }
    return render(request, 'prodigy/index.html', context)
def register(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if not User.objects.filter(username=username).exists():
            if password1 == password2:
                user = User.objects.create_user(username, email, password1)
                user.save()
    return render(request=request, template_name='prodigy/register.html', context={})

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            djangoLogin(request, user)
    return render(request, 'prodigy/login.html', context={})