from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('criar/', views.Criar.as_view(), name='criar'),
]
