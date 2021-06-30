from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema django2',
            body=conteudo,
            from_email='wesleygurgel27@gmail.com',
            to=['wesleygurgel27@gmail.com', ],
            headers={'Reply-TO': email}
        )

        mail.send()
