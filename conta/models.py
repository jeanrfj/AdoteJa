from django.db import models
from contatos.models import Contato
from animal.models import Animal
from django import forms


# Create your models here.


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar','categoria')

class FormCadastroAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ('slug',)