from turtle import home
from django.contrib import admin
from django.urls import path
from mundo1real.views import cadastrar_usuario
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login.html/', views.login_views, name='login_html'),
    path('login/', views.fazer_login, name='fazer_login'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cozinha/', views.cozinha_page, name='cozinha'),
    path('escritorio/', views.escritorio_page, name='cozinha'),
    path('eletronicos/', views.eletronicos_page, name='cozinha'),
    path('esportivos/', views.esportivos_page, name='cozinha'),
    path('brinquedos/', views.brinquedos_page, name='cozinha'),
    path('decoracao/', views.decoracao_page, name='cozinha'),
    path('carpintaria/', views.carpintaria_page, name='cozinha'),
]
