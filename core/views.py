from django.contrib import messages
from django.shortcuts import render
from core.forms import ContatoForm, ProdutoModelForm
from .models import Produto


# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail Enviado com Sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar E-mail!')

    context = {
        'formulario': form
    }

    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save()
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            print(form.cleaned_data)
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()

    context = {'form': form}
    return render(request, 'produto.html', context)
