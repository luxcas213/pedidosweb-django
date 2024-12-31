from django.urls import path
from . import views

urlpatterns = [
    path('platos/', views.getplatos, name='getplatos'),
    path('plato/<int:id>/', views.getplato, name='getplato'),
    path('updateplato/<int:id>/', views.updateplato, name='updateplato'),
    path('deleteplato/<int:id>/', views.deleteplato, name='deleteplato'),
    path('createplato/', views.createplato, name='createplato'),
    path('createpedido/', views.createpedido, name='createpedido'),
    path('pedidos/', views.getpedidosbyuser, name='getpedidos'),
    path('pedidos/<int:id>/', views.getpedidosbyid, name='getpedidobyid'),
    path('pedidos/user/', views.getpedidosbyuser, name='getpedidosbyuser'),
    path('pedidos/cambiarestado/<int:id>/', views.cambiar_estado, name='cambiarestado'),
    path('pedidos/delete/<int:id>/', views.deletepedido, name='deletepedido'),
    
]
