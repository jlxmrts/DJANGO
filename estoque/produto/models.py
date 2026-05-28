from django.db import models 

class Cores(models.Model): 
    cor = models.CharField('Cor', max_length=200) 
    def __str__(self): 
        return self.cor 
    
class Produtos(models.Model): 
    produto = models.CharField('Produto', max_length=200) 
    cor = models.ForeignKey(Cores, on_delete=models.PROTECT, verbose_name='Cor') 
    descricao = models.TextField('Descrição', blank=True) 
    preco = models.FloatField('Preço', default=0) 
    quantidade = models.IntegerField('Quantidade', default=0) 
    criado = models.DateTimeField('Criado em', auto_now_add=True) 
    modificado = models.DateTimeField('Modificado em', auto_now=True) 

    def __str__(self): 
        return self.produto 
    
    def precoQuantidade(self): 
        return self.preco * self.quantidade 
    
    class Meta: 
        verbose_name = 'Produto' 
        verbose_name_plural = 'Produtos' 
        ordering = ['-produto'] 