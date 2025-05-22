from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('visualizar/', views.Visualizar.as_view(), name='visualizar'),
]
