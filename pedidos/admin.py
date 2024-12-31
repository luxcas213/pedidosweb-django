from django.contrib import admin
from .models import Pedidos, Platos, PlatosXPedidos
# Register your models here.

admin.site.register(Pedidos)
admin.site.register(Platos)
admin.site.register(PlatosXPedidos)
