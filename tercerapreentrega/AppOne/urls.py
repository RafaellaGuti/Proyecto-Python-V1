from django.urls import path
from AppOne import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('productos/', views.productos, name='Productos'),
    path('servicios/', views.servicios, name='Servicios'),
    path('clientes/', views.clientes, name='Clientes'),
    path('busquedacategoria/', views.busquedacategoria, name='Busquedacategoria'),
    path('buscar/', views.buscar, name='Buscar')
    #path('productosform/', views.productosform, name= 'Productosform'),
    #path('serviciosform/', views.serviciosform, name= 'Serviciosform'),
    #path('clientesform/', views.clientesform, name= 'Clientesform'),


    
]
