from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cars.models import Car
# from django.db.models.signals import pre_save, pre_delete



# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     print('### PRE SAVE ###')
#     print(instance)

    
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    
    
    

# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     print('### PRE DELETE ###')
#     print(instance)
    
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### POST DELETE ###')
    print(instance)
    
    