from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .models import FormContato
from . import models
from django.contrib import messages
from django.shortcuts import render, redirect


class ListaAnimal(ListView):
    model = models.Animal
    template_name = 'animal/lista.html'
    context_object_name = 'animais'


class DetalheAnimal(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')


class AdicionarAnimal(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar Carrinho')


class RemoverAnimal(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover Carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')


def registrarInteresse(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)
        return render(request, 'dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter mais que 5 caracteres.')
        form = FormContato(request.POST)
        return render(request, 'dashboard.html', {'form': form})

    form.save()
    messages.success(
        request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard')
