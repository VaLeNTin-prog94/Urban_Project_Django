from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'index2.html')
