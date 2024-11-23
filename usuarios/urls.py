""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ver_all/', views.ver_usuarios, name='ver_all'),
    path('form/', views.ver_cadastro, name='form'),
    path('cadastro/', views.insere_user, name='cadastro'),
    # path('ver-all/', views.ver_usuarios, name='ver-all'),
    path('seeds/', views.seeds, name='seeds'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
