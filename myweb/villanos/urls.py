#Este archivo lo creamos nosotros, no viene por defecto xq podemos no necesitarlo.
from django.urls import path
from villanos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ahora', views.vista_hoy, name='vista_hoy'),
    path('list', views.list, name='list'),
]