from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from cars.models import Car

@csrf_protect
def cars(request):
  # cars = Car.objects.all() # pegando todos os dados
  # cars = Car.objects.filter(brand__name='Fiat') # filtrando os dados usando o __ + o campo, navegando entre tabelas.
  cars = Car.objects.filter(brand='2') # filtrando os dados
  cars = Car.objects.filter(model='Chevette tubarão') # filtrando pelo modelo
  cars = Car.objects.filter(model__contains='Chevette tubarão') # filtrando pelo modelo
  


  return render(request,'cars.html', {'cars': cars})
