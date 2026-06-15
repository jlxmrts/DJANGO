from django.db import models
from produto.models import Produtos

class Saidas(models.Model):
    produto = models.ForeignKey(
        Produtos,
        on_delete=models.CASCADE,
        verbose_name='Produto'
    )

    quantidade = models.IntegerField(
        'Quantidade',
        default=0
    )

    criado = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    modificado = models.DateTimeField(
        'Modificado em',
        auto_now=True
    )

    def __str__(self):
        return f'{self.produto} - {self.quantidade}'