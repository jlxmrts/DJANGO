from django.forms import ModelForm, TextInput 
from .models import Produtos 

class ProdutoForm(ModelForm): 
    class Meta: 
        model = Produtos 
        fields = ['produto', 'cor', 'descricao'] 
        widgets ={
            'produto': TextInput(attrs={
                'class': 'class' #declara classe - nome da classe (class)
            })
        }