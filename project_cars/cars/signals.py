from django.db.models.signals import pre_save, pre_delete, post_save, post_delete

def car_pre_save(sender, intance, **kwargs):
    print('### PRE SAVE ###')