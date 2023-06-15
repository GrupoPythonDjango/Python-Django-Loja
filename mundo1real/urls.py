from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('login/', views.login_views, name='login'),
path('fazerlogin/', views.fazer_login, name='fazer_login'),
path('cadastro/', views.cadastro_views, name='cadastro'),
path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
path('cozinha/', views.cozinha_page, name='cozinha'),
path('escritorio/', views.escritorio_page, name='escritorio'),
path('eletronicos/', views.eletronicos_page, name='eletronicos'),
path('esportivos/', views.esportivos_page, name='esportivos'),
path('brinquedos/', views.brinquedos_page, name='brinquedos'),
path('decoracao/', views.decoracao_page, name='decoracao'),
path('carpintaria/', views.carpintaria_page, name='carpintaria'),


]
