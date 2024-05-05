from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car


def cars(request):
  cars = Car.objects.all().order_by('model') # pegando todos os dados e usando afunçao (oder_by) para ordenar pelo modelo.(-model)faz ordenaçao contraria de Z a A.

  # Fazendo o usuario conseguir filtrar pela requisiçao(capturando o request e aplicando o filtro)
  search = request.GET.get('search') #o usuario esta mando um parametro =(search) que esta querendo filtrar 
  
  if search: # verificar se o usuario passar marametros , aplique o filtro na request recebida(__icontains =caixa alta ou caixa baixa)
    cars = Car.objects.filter(model__icontains=search).order_by('model') # filtro no campo modelo do banco e pegando qualquer campo com __contains + o parametro search
  
  
  # print(request.GET) # visualizando a lista(completa) de querys que o usuario passou
  # print(request.GET.get('search')) # capturando parametros da requisicao GET do usuario
  # cars = Car.objects.filter(brand__name='Fiat') # filtrando os dados usando o __ + o campo, navegando entre tabelas.
  # cars = Car.objects.filter(brand='2') # filtrando os dados pelo id
  # cars = Car.objects.filter(model='Chevette tubarão') # filtrando pelo modelo
  # cars = Car.objects.filter(model__contains='C') # filtrando pela função (__contains) para pegar qualquer campo que comece com a string passada


  # retornando a renderizaçao da pagina com o template e as informaçoes armazenadas na viavel (cars)
  return render(request,'base.html', {'cars': cars})
