from django import forms


class SubscriptionForm(forms.Form):  # forms.Form É a classe base de formulários do Django
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
