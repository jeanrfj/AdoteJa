from django.db import models
from contatos.models import Contato
from animal.models import Animal
from django import forms


# Create your models here.


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar', 'categoria')


class FormCadastroAnimal(forms.ModelForm):
    # data_nascimento = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'}),
    #     input_formats=['%Y-%m-%d'],
    #     help_text='YYYY-MM-DD'
    # )

    ativo = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = Animal
        exclude = ('slug', 'user', 'ativo')

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')
            super().__init__(*args, **kwargs)
            self.instance.user = user
