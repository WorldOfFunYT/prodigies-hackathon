from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login


# Create your views here.

def index(request):
    context = {
        
    }
    return render(request, 'prodigy/index.html', context)
def register(request):
    return render(request=request, template_name='prodigy/register.html', context={})