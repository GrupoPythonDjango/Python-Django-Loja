from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_pro', views.cadastro_pro, name='cadastro_pro'),
]