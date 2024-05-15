from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
# from cars.forms import CarForm
from cars.forms import CarModelForm
from django.views import View



# usando Function Based views
# def cars(request):
  # cars = Car.objects.all().order_by('model') # pegando todos os dados e usando afunçao (oder_by) para ordenar pelo modelo.(-model)faz ordenaçao contraria de Z a A.

  # Fazendo o usuario conseguir filtrar pela requisiçao(capturando o request e aplicando o filtro)
  # search = request.GET.get('search') #o usuario esta mando um parametro =(search) que esta querendo filtrar 
  
  # if search: # verificar se o usuario passar marametros , aplique o filtro na request recebida(__icontains =caixa alta ou caixa baixa)
    # cars = Car.objects.filter(model__icontains=search).order_by('model') # filtro no campo modelo do banco e pegando qualquer campo com __contains + o parametro search
  
  
  # print(request.GET) # visualizando a lista(completa) de querys que o usuario passou
  # print(request.GET.get('search')) # capturando parametros da requisicao GET do usuario
  # cars = Car.objects.filter(brand__name='Fiat') # filtrando os dados usando o __ + o campo, navegando entre tabelas.
  # cars = Car.objects.filter(brand='2') # filtrando os dados pelo id
  # cars = Car.objects.filter(model='Chevette tubarão') # filtrando pelo modelo
  # cars = Car.objects.filter(model__contains='C') # filtrando pela função (__contains) para pegar qualquer campo que comece com a string passada


  # retornando a renderizaçao da pagina com o template e as informaçoes armazenadas na viavel (cars)
  # return render(request,'cars.html', {'cars': cars})



# Usano Class Bases Views no Lugar de Function Based Views(Boa Prática)
class CarsView(View):
  
  def get(self, request):
    cars = Car.objects.all().order_by('model') 
    search = request.GET.get('search') 
    
    if search: 
      cars = cars.filter(model__icontains=search) 
    return render(request,'cars.html', {'cars': cars})



# com apenas Form
# def new_car_view(request):
#   if request.method == 'POST':
#     new_car_form= CarForm(request.POST, request.FILES)
#     if new_car_form.is_valid(): # se os dados forem validos, chame a funcao save
#       new_car_form.save() # salva no database
#       return redirect('cars_list') # redireciona o usuario para a pagina principal da lista dos carros
#   else:
#     new_car_form = CarForm() # cria um formulario vazio
#   return render(request, 'new_car.html', { 'new_car_form': new_car_form }) # passando o formulario para o template




# Com ModelForm
def new_car_view(request):
  if request.method == 'POST':
    new_car_form= CarModelForm(request.POST, request.FILES)
    if new_car_form.is_valid(): # se os dados forem validos, chame a funcao save
      new_car_form.save() # salva no database
      return redirect('cars_list') # redireciona o usuario para a pagina principal da lista dos carros
  else:
    new_car_form = CarModelForm() # cria um formulario vazio
  return render(request, 'new_car.html', { 'new_car_form': new_car_form }) # passando o formulario para o template

