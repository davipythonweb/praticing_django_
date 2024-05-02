from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from cars.models import Car

@csrf_protect
def cars(request):
  cars = Car.objects.all()
  print(cars)
  return render(request,'cars.html', {'cars': {'model': 'Astra 2.0'}})
