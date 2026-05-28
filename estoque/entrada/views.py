from django.shortcuts import render, redirect 
from .models import Entradas 
from .forms import EntradaForm 
def list_entrada(request): 
    entradas = Entradas.objects.all() 
    template_name = 'list_entrada.html' 
    context = { 
    'entradas': entradas, 
} 
    return render(request, template_name, context) 

def new_entrada(request): 
    if request.method == 'POST': 
        form = EntradaForm(request.POST) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + form.cleaned_data['quantidade'] 
            form.cleaned_data['produto'].preco = form.cleaned_data['preco'] 
            form.cleaned_data['produto'].save_base() 
            form.save() 
            return redirect('entrada:list_entrada') 
    else: 
        template_name = 'form_entrada.html' 
        context = { 
        'form': EntradaForm(), 
      } 
        return render(request, template_name, context) 
 
def update_entrada(request, pk): 
    entrada = Entradas.objects.get(pk=pk) 
    quantidade = entrada.quantidade 
    print('==> ', quantidade) 
    if request.method == 'POST': 
        form = EntradaForm(request.POST, instance=entrada) 
        if form.is_valid(): 
            print('===> ', quantidade, form.cleaned_data['quantidade']) 
            form.save(commit=False) 
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - quantidade + form.cleaned_data['quantidade'] 
            form.cleaned_data['produto'].save_base() 
            form.save() 
            return redirect('entrada:list_entrada') 
    else: 
        template_name = 'form_entrada.html' 
        context = { 
          'form': EntradaForm(instance=entrada), 
          'pk': pk, 
        } 
        return render(request, template_name, context) 
    
def delete_entrada(request, pk): 
    entrada = Entradas.objects.get(pk=pk) 
    entrada.produto.quantidade = entrada.produto.quantidade - entrada.quantidade 
    entrada.produto.save() 
    entrada.delete() 
    return redirect('entrada:list_entrada') 