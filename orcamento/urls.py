from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lista_despesas', views.lista_despesas, name='lista_despesas'),
    ]