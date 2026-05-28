from django.db import models 
from produto.models import Produtos 

class Entradas(models.Model): 
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name='Produto') 
    preco = models.FloatField('Preço', default=0) 
    quantidade = models.IntegerField('Quantidade', default=0) 
    criado = models.DateTimeField('Criado em', auto_now_add=True) 
    modificado = models.DateTimeField('Modificado em',auto_now=True) 