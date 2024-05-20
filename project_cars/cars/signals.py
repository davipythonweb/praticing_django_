from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory

from django.db.models import Sum


def car_invetory_update():
    cars_count = Car.objects.all().count() # calcula a qtd de carros no estoque
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] # calcula o o valor total da soma(R$) dos carros do estoque
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value) # cria a nova tabela no banco
    
    
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_invetory_update()
    
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_invetory_update()
    