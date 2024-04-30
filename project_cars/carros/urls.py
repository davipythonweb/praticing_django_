from django.urls import path
from .views import carros

urlpatterns = [
  path('', carros),
]