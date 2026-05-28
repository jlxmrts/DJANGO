from django.forms import ModelForm 
from .models import Entradas 
class EntradaForm(ModelForm): 
    class Meta: 
        model = Entradas 
        fields = ['produto', 'quantidade', 'preco']