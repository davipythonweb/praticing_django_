from django.shortcuts import render
from django.http import HttpResponse

def carros(request):
  return HttpResponse('Ola Django')
