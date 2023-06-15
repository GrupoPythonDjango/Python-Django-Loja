from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from .models import Usuario
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')


def login_views(request):
    return render(request, 'login.html')

def cadastro_views(request):
    return render (request, 'cadastro.html')

#fim da def home e login

# def de departamentos

def cozinha_page(request):
    return render(request, './departamentos/depart_cozinha.html')

def brinquedos_page(request):
    return render(request, 'departamentos/depart_brinquedos.html')

def carpintaria_page(request):
    return render(request, 'departamentos/depart_carpintaria.html')

def decoracao_page(request):
    return render(request, 'departamentos/depart_decoracao.html')

def eletronicos_page(request):
    return render(request, 'departamentos/depart_eletronicos.html')

def escritorio_page(request):
    return render(request, 'departamentos/depart_escritorio.html')

def esportivos_page(request):
    return render(request, 'departamentos/depart_esportivos.html')

# fim def de  departamentos


def cadastrar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        nome = request.POST['nome']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if senha == confirmar_senha:
            senha_hash = make_password(senha)

            usuario = Usuario(email=email, nome=nome, senha=senha_hash)
            usuario.save()

            return redirect('home')
        else:
            return render(request, 'erro.html')
    else:
        return render(request, 'home.html')
    
def fazer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            print('Login bem-sucedido')  # Adicione esse print para verificar se o login está sendo feito corretamente
            return redirect('home.html')
        else:
            print('deu merda')  # Adicione esse print para verificar se as credenciais estão sendo validadas corretamente
            return render(request, 'erro.html', {'erro': 'Credenciais inválidas'})
    else:
        return render(request, 'home.html')
