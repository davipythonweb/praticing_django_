from django import forms
# from cars.models import Brand
from cars.models import Car


# A mesma solução resumida com (ModelForm)
class CarModelForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'


  def clean_value(self): # validaçao de formulario (valor do carro)
    value = self.cleaned_data.get('value')
    if value < 20000:
      self.add_error('value', 'Valor mínimo de carro deve ser de R$20.000.')
    return value

  def clean_factory_year(self): # validaçao do ano de fabricação
    factory_year = self.cleaned_data.get('factory_year')
    if factory_year < 1975:
      self.add_error('factory_year', 'Não é possivel cadastrar carros fabricados antes de 1975.')
    return factory_year




#regra: não eh possivel cadastrar carro com valor abaixo de $20.000 reais. 
# carros com ano menor que 1975 não pode ser cadastrados

"""
todo este código para trabalhar com (Form)
"""
# class CarForm(forms.Form):
#   model = forms.CharField(max_length=200)
#   brand = forms.ModelChoiceField(Brand.objects.all()) # mostrar para o usuario uma lista de opçoes da query feita na tabela
#   factory_year = forms.IntegerField()
#   model_year = forms.IntegerField()
#   plate = forms.CharField(max_length=10)
#   value = forms.FloatField()
#   photo = forms.ImageField()

#   def save(self): # cria um objeto cars , que recebe todos os campos para criar um carro novo
#     car = Car(
#       model = self.cleaned_data['model'],
#       brand = self.cleaned_data['brand'],
#       factory_year = self.cleaned_data['factory_year'],
#       model_year = self.cleaned_data['model_year'],
#       plate = self.cleaned_data['plate'],
#       value = self.cleaned_data['value'],
#       photo = self.cleaned_data['photo'],
#     )
#     car.save() # salva no database
#     return car # retornando entao , o objeto que foi criado



