from django.urls import path, include
from .views import cars
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', cars),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # para configurar uso de armazenar

