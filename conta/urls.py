from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    # path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('perfil/', views.atualizarCadastro, name='atualizar_perfil'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/animais/', views.dashboardAnimais, name='dashboard-animais'),
    path('dashboard/animais/cadastrar/', views.dashboardAnimaisCadastrar,
         name='dashboard-animais-cadastrar'),
    path('dashboard/animais/editar/<int:animal_id>', views.dashboardAnimaisEditar,
         name='dashboard-animais-editar'),
    path('dashboard/interessados/', views.dashboardInteressados,
         name='dashboard-interessados'),
    path('excluir-animal/<int:animal_id>/', views.excluir_animal, name='excluir-animal'),
]