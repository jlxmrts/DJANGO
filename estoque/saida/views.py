from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidaForm


def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {
        'saidas': saidas,
    }

    return render(request, template_name, context)


def new_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']
            # verifica estoque
            if produto.quantidade >= quantidade:
                form.save(commit=False)
                # diminui estoque
                produto.quantidade = produto.quantidade - quantidade
                produto.save()
                form.save()
                return redirect('saida:list_saida')

            else:
                context = {
                    'form': form,
                    'error': 'Quantidade insuficiente no estoque'
                }
                return render(request, 'form_saida.html', context)

    else:
        template_name = 'form_saida.html'
        context = {
            'form': SaidaForm(),
        }
        return render(request, template_name, context)


def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    quantidade_antiga = saida.quantidade
    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            nova_quantidade = form.cleaned_data['quantidade']
            diferenca = nova_quantidade - quantidade_antiga

            # verifica se há estoque suficiente
            if produto.quantidade >= diferenca:
                form.save(commit=False)
                produto.quantidade = produto.quantidade - diferenca
                produto.save()
                form.save()

                return redirect('saida:list_saida')

            else:
                context = {
                    'form': form,
                    'pk': pk,
                    'error': 'Estoque insuficiente'
                }
                return render(request, 'form_saida.html', context)

    else:
        template_name = 'form_saida.html'
        context = {
            'form': SaidaForm(instance=saida),
            'pk': pk,
        }
        return render(request, template_name, context)


def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    # devolve ao estoque
    saida.produto.quantidade = (
        saida.produto.quantidade + saida.quantidade
    )

    saida.produto.save()
    saida.delete()
    return redirect('saida:list_saida')