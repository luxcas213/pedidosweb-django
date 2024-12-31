from django import forms
from .models import Pedidos, Platos, PlatosXPedidos



class PlatosForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = '__all__'

class PlatosXPedidosForm(forms.ModelForm):
    class Meta:
        model = PlatosXPedidos
        fields = '__all__'
