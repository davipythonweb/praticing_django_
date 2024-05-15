from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from cars.views import cars, new_car_view
from accounts.views import register_view, login_view, logout_view
from cars.views import CarsView, new_car_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', CarsView.as_view(), name='cars_list'),
    path('new_car/',new_car_view, name='new_car'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # para configurar uso de armazenar
