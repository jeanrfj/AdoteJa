from django.urls import path
from . import views

app_name = 'animal'

urlpatterns = [
    path('', views.ListaAnimal, name='lista'),
    path('<slug>', views.DetalheAnimal.as_view(), name='detalheanimal'),
    path('interesse/<int:id>/<str:nome>/',
         views.cadastroDeInteresse, name='interesse'),
    #     path('registrar-interesse/<str:nome>/',
    #          views.registrarInteresse, name='registrar-interesse'),
    path('registrar-interesse/<int:id_animal>/',
         views.registrarInteresse, name='registrar-interesse'),
    path('adicionaranimal/', views.AdicionarAnimal.as_view(), name='adicionaranimal'),
    path('removeranimal/', views.RemoverAnimal.as_view(), name='removeranimal'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]
