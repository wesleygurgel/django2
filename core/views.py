from django.contrib import messages
from django.shortcuts import render
from core.forms import ContatoForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada: ')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail Enviado com Sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar E-mail!')

    context = {
        'formulario': form
    }

    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
