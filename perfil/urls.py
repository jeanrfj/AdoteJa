from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('criar/',views.Criar.as_view(),name='criar'),
    #path('perfil/atualizar/',views.Atualizar.as_view(),name='atualizar')
]