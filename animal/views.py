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


def cadastroDeInteresse(request, nome, id):
    if request.method != 'POST':
        return render(request, 'interesse.html', {'nome': nome, 'id': id})


def registrarInteresse(request, nome):
    if request.method == 'POST':
        # acao = 'Cadastro Con'
        messages.success(
            request, f'Interesse em {nome} registrado com sucesso!')
        return render(request, 'interesse-registrado.html')

    # form = FormContato(request.POST, request.FILES)

    # if not form.is_valid():
    #     messages.error(request, 'Erro ao enviar formulário.')
    #     form = FormContato(request.POST)
    #     return render(request, 'dashboard.html', {'form': form})

    # descricao = request.POST.get('descricao')

    # if len(descricao) < 5:
    #     messages.error(request, 'Descrição precisa ter mais que 5 caracteres.')
    #     form = FormContato(request.POST)
    #     return render(request, 'dashboard.html', {'form': form})

    # form.save()
    # messages.success(
    #     request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    # return redirect('dashboard')


# def registrarInteresse(request):
#     if request.method != 'POST':
#         form = FormContato()
#         return render(request, 'interesse.html', {'form': form})

#     form = FormContato(request.POST, request.FILES)

#     if not form.is_valid():
#         messages.error(request, 'Erro ao enviar formulário.')
#         form = FormContato(request.POST)
#         return render(request, 'dashboard.html', {'form': form})

#     descricao = request.POST.get('descricao')

#     if len(descricao) < 5:
#         messages.error(request, 'Descrição precisa ter mais que 5 caracteres.')
#         form = FormContato(request.POST)
#         return render(request, 'dashboard.html', {'form': form})

#     form.save()
#     messages.success(
#         request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
#     return redirect('dashboard')
