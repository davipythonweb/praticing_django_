from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def cars(request):
  return HttpResponse('<h1>Ola Django</h1>')
