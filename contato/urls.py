from django.urls import path
from . import views

urlpatterns = [
    path('', views.contatoSite, name='contato'),
]
