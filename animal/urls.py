from django.urls import path
from . import views

app_name = 'animal'

urlpatterns = [
    path('', views.ListaAnimal.as_view(), name='lista'),
    path('<slug>', views.DetalheAnimal.as_view(), name='detalheanimal'),
    path('interesse/', views.registrarInteresse, name='interessados'),
    path('adicionaranimal/', views.AdicionarAnimal.as_view(), name='adicionaranimal'),
    path('removeranimal/', views.RemoverAnimal.as_view(), name='removeranimal'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]
