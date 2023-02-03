from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Olá Django')
# Create your views here.
