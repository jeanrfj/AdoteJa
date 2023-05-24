from . import models
from django.shortcuts import get_object_or_404, render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .models import FormContato, Contato, FormCadastroAnimal, Animal, EditarAnimal
from animal.models import Interessados
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserChangeForm
from django.db.models import Q


def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('dashboard-animais')


def logout(request):
    auth.logout(request)
    # messages.success(request, 'Você fez logout com sucesso.')
    return redirect('/conta/login/')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha \
            or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe.')
        return render(request, 'cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required
def excluir_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    animal.delete()
    return redirect('dashboard-animais')


@login_required
def atualizarCadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if not nome or not sobrenome or not email or not usuario:
            messages.error(request, 'Nenhum campo pode estar vazio.')
            return render(request, 'perfil.html')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Email inválido.')
            return render(request, 'perfil.html')

        user = request.user
        user.first_name = nome
        user.last_name = sobrenome
        user.email = email
        user.username = usuario

        if senha:
            if len(senha) < 6:
                messages.error(
                    request, 'Senha precisa ter 6 caracteres ou mais.')
                return render(request, 'perfil.html')
            if senha != senha2:
                messages.error(request, 'Senhas não conferem.')
                return render(request, 'perfil.html')
            user.set_password(senha)

        user.save()
        messages.success(request, 'Dados atualizados com sucesso.')
        return render(request, 'perfil.html')

    return render(request, 'perfil.html')


""" @login_required(redirect_field_name='login')
def dashboard(request):
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
 """


@login_required(redirect_field_name='login')  # Lista de animais no dasboard
def dashboardAnimais(request):
    user = request.user
    obj = request.GET.get('obj')

    if obj:
        animais_pag = models.Animal.objects.filter(
            (Q(nome_animal__icontains=obj) |
             Q(descricao__icontains=obj) |
             Q(especie__icontains=obj[0]) |
             Q(raca__icontains=obj) |
             Q(cor__icontains=obj) |
             Q(porte__icontains=obj) |
             Q(sexo__icontains=obj[0]) |
             Q(peso__icontains=obj) |
             Q(castrado__icontains=obj) |
             Q(status_adocao_animal__icontains=obj[0]) |
             Q(data_nascimento__icontains=obj)) & Q(user=request.user))
    else:
        animais_pag = Animal.objects.filter(user=request.user).order_by('-id')

    animais_paginator = Paginator(animais_pag, 10)
    page_num = request.GET.get('page')
    page = animais_paginator.get_page(page_num)
    return render(request, 'listar-animais.html', {'page': page, 'obj': obj})


"""
@login_required(redirect_field_name='login') #Lista de animais no dasboard
def dashboardAnimais(request):
    user = request.user
    animais = Animal.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(animais, 20)

    page = request.GET.get('p')
    animais = paginator.get_page(page)

    return render(request, 'listar-animais.html', {
        'animais': animais
    })
 """


@login_required(redirect_field_name='login')
def dashboardAnimaisCadastrar(request):
    if request.method == 'POST':
        form = FormCadastroAnimal(request.POST, request.FILES)

        if form.is_valid():
            animal = form.save(commit=False)
            animal.user = request.user
            animal.save()
            messages.success(request, 'Animal cadastrado com sucesso.')
            return redirect('/conta/dashboard/animais')
        else:
            messages.error(request, 'erro ao cadastrar animal !')
    else:
        form = FormCadastroAnimal()
    return render(request, 'cadastrar-animal.html', {'form': form})


@login_required(redirect_field_name='login')
def dashboardAnimaisEditar(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        form = EditarAnimal(request.POST, request.FILES, instance=animal)

        if form.is_valid():
            form.save()
            messages.success(request, 'Animal editado com sucesso.')
            return redirect('dashboard-animais')
        else:
            messages.error(request, 'Erro ao editar animal!')
    else:
        form = EditarAnimal(instance=animal)

    return render(request, 'editar-animal.html', {'form': form})


def dashboardInteressados(request):
    obj = request.GET.get('obj')

    interessados = Interessados.objects.filter(proprietario=request.user).order_by('-id')
    paginator = Paginator(interessados, 10)
    page = request.GET.get('page')
    interessados = paginator.get_page(page)
    return render(request, 'interessados.html', {
        'interessados': interessados
    })




def dashboardInteressadosEmUmAnimal(request, animal_id):
    interessados = Interessados.objects.filter(
        proprietario_id=request.user.id, animal_id=animal_id).order_by('-id')

    paginator = Paginator(interessados, 20)

    page = request.GET.get('p')
    interessados = paginator.get_page(page)

    # Obter o objeto Animal correspondente ao animal_id
    animal = Animal.objects.get(id=animal_id)

    return render(request, 'interessados.html', {
        'interessados': interessados,
        # Passar o nome do animal como contexto para o template
        'animal_nome': animal.nome_animal
    })
