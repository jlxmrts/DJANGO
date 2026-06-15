from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidaForm


def list_saida(request):
    saidas = Saidas.objects.all()

    return render(
        request,
        'list_saida.html',
        {'saidas': saidas}
    )


def new_saida(request):

    if request.method == 'POST':

        form = SaidaForm(request.POST)

        if form.is_valid():

            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']

            if produto.quantidade < quantidade:

                return render(
                    request,
                    'form_saida.html',
                    {
                        'form': form,
                        'error': 'Quantidade insuficiente no estoque'
                    }
                )

            produto.quantidade -= quantidade
            produto.save()

            form.save()

            return redirect('saida:list_saida')

    return render(
        request,
        'form_saida.html',
        {
            'form': SaidaForm()
        }
    )


def update_saida(request, pk):

    saida = Saidas.objects.get(pk=pk)

    quantidade_antiga = saida.quantidade

    if request.method == 'POST':

        form = SaidaForm(
            request.POST,
            instance=saida
        )

        if form.is_valid():

            produto = form.cleaned_data['produto']
            nova_quantidade = form.cleaned_data['quantidade']

            estoque_final = (
                produto.quantidade
                + quantidade_antiga
                - nova_quantidade
            )

            if estoque_final < 0:

                return render(
                    request,
                    'form_saida.html',
                    {
                        'form': form,
                        'pk': pk,
                        'error': 'Estoque insuficiente'
                    }
                )

            produto.quantidade = estoque_final
            produto.save()

            form.save()

            return redirect('saida:list_saida')

    return render(
        request,
        'form_saida.html',
        {
            'form': SaidaForm(instance=saida),
            'pk': pk,
        }
    )


def delete_saida(request, pk):

    saida = Saidas.objects.get(pk=pk)

    saida.produto.quantidade += saida.quantidade

    saida.produto.save()

    saida.delete()

    return redirect('saida:list_saida')