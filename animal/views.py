from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.http import HttpResponse
from .models import FormContato
from .models import Interessados, Animal
from . import models
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q


""" class ListaAnimal(ListView):
    model = models.Animal
    template_name = 'animal/lista.html'
    context_object_name = 'animais'
 """


def ListaAnimal(request):
    obj = request.GET.get('obj')

    if obj:
        animais_pag = models.Animal.objects.filter(
            Q(nome_animal__icontains=obj) |
            Q(descricao__icontains=obj) |
            Q(especie__icontains=obj[0]) |
            Q(raca__icontains=obj) |
            Q(cor__icontains=obj) |
            Q(porte__icontains=obj) |
            Q(sexo__icontains=obj[0]) |
            Q(peso__icontains=obj) |
            Q(castrado__icontains=obj) |
            Q(data_nascimento__icontains=obj))
    else:
        animais_pag = models.Animal.objects.all()

    animais_paginator = Paginator(animais_pag, 6)
    page_num = request.GET.get('page')
    page = animais_paginator.get_page(page_num)
    return render(request, 'animal/lista.html', {'page': page, 'obj': obj})


class DetalheAnimal(DetailView):
    model = models.Animal
    template_name = 'animal/detalhe.html'
    slug_url_kwarg = 'slug'


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


def registrarInteresse(request, id_animal):
    print(request)
    animal = get_object_or_404(Animal, id=id_animal)

    if request.method == 'POST':
        nome = request.POST['nome']
        endereco = request.POST['endereco']
        data_de_nascimento = request.POST['data_de_nascimento']
        telefone = request.POST['telefone']
        email = request.POST['email']
        mensagem = request.POST.get(
            'mensagem', 'Tenho interesse no pet')

        interessado = Interessados(
            nome=nome,
            animal=animal,
            proprietario=animal.user,
            endereco=endereco,
            data_de_nascimento=data_de_nascimento,
            telefone=telefone,
            email=email,
            mensagem=mensagem
        )
        interessado.save()

        messages.success(
            request, f'Interesse em {animal.nome_animal} registrado com sucesso!')
        return render(request, 'interesse-registrado.html')

    # return render(request, 'seu-template.html', {'animal': animal})

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
