from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
        'mensagem': 'Bem-vindo ao sistema'
    }
    return render(request, template_name, context)