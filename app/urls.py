from django.urls import path, include
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('index2', index2, name='index2'),
    path('ventas', ventas, name="ventas"),
    path('articulosD', articulosD, name='articulosD'),
    path('historial', historial, name='historial'),
    path('carritoC', carritoC, name='carritoC'),
    path('usuario', usuario, name='usuario'),
    path('herramientas', herramientas, name='herramientas'),
    path('Sustrato', Sustrato, name='Sustrato'),
    path('Semillas', Semillas, name='Semillas'),
    path('seguimiento', seguimiento, name='seguimiento'),
    path('historial', historial, name='historial'),
    path('nProducto', nProducto, name='nProducto'),
    path('compras', compras, name='compras'),
    path('carritoC2', carritoC2, name='carritoC2'),
    path('confirmacion', confirmacion, name='confirmacion'),
    path('error', error, name='error'),
    path('registro', registro, name='registro'),
    path('suscripcion', suscripcion, name='suscripcion'),
    path('confirmacionS', confirmacionS, name='confirmacionS'),
    path('cancelarSuscripcion', cancelarSuscripcion, name='cancelarSuscripcion'),
    path('ConfirmacionCancelacion', ConfirmacionCancelacion, name='ConfirmacionCancelacion'),
    path('productoE', productoE, name='productoE'),
]