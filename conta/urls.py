from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    # path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    # path('perfil/', views.atualizarCadastro, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/animais/', views.dashboardAnimais, name='dashboard-animais'),
    path('dashboard/animais/cadastrar', views.dashboardAnimaisCadastrar,
         name='dashboard-animais-cadastrar'),
    path('dashboard/animais/deletar', views.dashboardAnimaisCadastrar,
         name='dashboard-animais-deletar'),
    path('dashboard/interessados/', views.dashboardInteressados,
         name='dashboard-interessados'),
    path('dashboard/perfil/', views.dashboardPerfil, name='dashboard-perfil'),
]
