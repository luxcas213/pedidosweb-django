from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedidos, Platos, PlatosXPedidos
from .forms import PlatosForm

# Mostrar todos los platos
def getplatos(request):
    platos = Platos.objects.all()
    return render(request, 'pedidos/platos.html', {"platos": platos})

# Mostrar un plato específico
def getplato(request, id):
    plato = get_object_or_404(Platos, id=id)
    return render(request, 'pedidos/plato.html', {"plato": plato})

# Actualizar un plato
def updateplato(request, id):
    plato = get_object_or_404(Platos, id=id)
    if request.method == 'POST':
        form = PlatosForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('getplatos')
    else:
        form = PlatosForm(instance=plato)
    return render(request, 'pedidos/updateplato.html', {"form": form})

# Eliminar un plato
def deleteplato(request, id):
    plato = get_object_or_404(Platos, id=id)
    plato.delete()
    return redirect('getplatos')

# Crear un nuevo plato
def createplato(request):
    if request.method == 'POST':
        form = PlatosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getplatos')
    else:
        form = PlatosForm()
    return render(request, 'pedidos/createplato.html', {"form": form})

# Crear un pedido
def createpedido(request):
    if request.method == 'POST':
            # Obtener platos y cantidades
            platos_ids = request.POST.getlist('platos')
            cantidades = request.POST.getlist('cantidades')
            pedido=Pedidos.objects.create(
                    user=request.user
                )
            for i in range(len(platos_ids)):
                plato = Platos.objects.get(id=platos_ids[i])
                
                PlatosXPedidos.objects.create(
                    pedido=pedido,
                    plato=plato,
                    cantidad=cantidades[i]
                )
            return redirect('getpedidos')
    else:
        platos = Platos.objects.all()
    return render(request, 'pedidos/createpedido.html', {
        'platos': platos
    })

# Mostrar todos los pedidos
def getpedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/pedidos_list.html', {"pedidos": pedidos})

def getpedidosbyuser(request):
    pedidos = Pedidos.objects.filter(user=request.user)
    return render(request, 'pedidos/pedidos_list.html', {"pedidos": pedidos})

def getpedidosbyid(request, id):
    pedido=Pedidos.objects.get(id=id)
    pedido=[pedido]
    return render(request, 'pedidos/pedidos_list.html', {"pedidos": pedido})

def cambiar_estado(request, id):
    pedido = Pedidos.objects.get(id=id)
    if pedido.estado == "pendiente":
        pedido.estado = "entregado"
    else:
        pedido.estado = "pendiente"
    pedido.save()
    return redirect('getpedidos')
    
def deletepedido(request, id):
    pedido = get_object_or_404(Pedidos, id=id)
    pedido.delete()
    return redirect('getpedidos')