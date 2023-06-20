from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),  # Renomeada para login_view
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('fazer_login/', views.fazer_login, name='fazer_login'),
    path("sair/", views.sair, name="sair"),

    path('produto/', views.produto_page, name='produto_page'),
    path('cozinha/', views.cozinha_page, name='cozinha'),
    path('escritorio/', views.escritorio_page, name='escritorio'),
    path('eletronicos/', views.eletronicos_page, name='eletronicos'),
    path('esportivos/', views.esportivos_page, name='esportivos'),
    path('brinquedos/', views.brinquedos_page, name='brinquedos'),
    path('decoracao/', views.decoracao_page, name='decoracao'),
    path('carpintaria/', views.carpintaria_page, name='carpintaria'),
    path('search/', views.search_product, name='search_product'),
]