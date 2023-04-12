from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeSite, name='home'),
]
