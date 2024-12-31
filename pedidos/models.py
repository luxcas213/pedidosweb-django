from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pedidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=100, default="pendiente")

    
class Platos(models.Model):
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
    
class PlatosXPedidos(models.Model):
    
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)
    def __str__(self):
        return self.plato.nombre + " - " + self.pedido.nombre + " - " + str(self.cantidad)