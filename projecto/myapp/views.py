from django.http import HttpResponse
from django.shortcuts import render

def hello(request , nombre):
    return HttpResponse('hola %s' % nombre)
# Create your views here.
