from django.shortcuts import render

# Create your views here.


def contatoSite(request):
    return render(request, 'contato.html')
