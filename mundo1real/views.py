from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from .models import Usuario
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')

def login_views(request):
    return render(request, 'login.html')

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

            return redirect('')
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
            return redirect('home')  # Redirecionar para a página inicial após o login
        else:
            # Exibir uma mensagem de erro para o usuário
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    else:
        return render(request, 'home')
