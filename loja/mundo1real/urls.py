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
]
