from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('menu', views.menu, name='menu'),
    path('change_pin', views.change_pin, name='change_pin')
]