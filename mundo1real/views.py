from itertools import product
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password

from mundo1real.form import ProductSearchForm
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
     if request.method == 'GET':
        query = request.GET.get('search_query')
        return render(request, 'depart_cozinha.html', {'query': query})
     else:
        return render(request, './departamentos/depart_cozinha.html')
     
def brinquedos_page(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')
        results = []
        
        if search_query:
            # Realizar a pesquisa de produtos de brinquedos com base no query de pesquisa
            results = Produto.objects.filter(nome__icontains=search_query, departamento='brinquedos')

        return render(request, 'search_results.html', {'query': search_query, 'results': results})
    else:
        # Renderizar o template para a página de Brinquedos
        return render(request, 'brinquedos.html')
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

# def de produtos

def produto_page(request):
    return render(request, 'produto.html')
# fim da def de produtos


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
    
    
def search_product(request):
    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Faça a lógica de pesquisa aqui com base na query fornecida pelo usuário
            # por exemplo, você pode pesquisar no banco de dados usando o modelo do produto
            products = product.objects.filter(name__icontains=search_query)
            # Renderize o template com os resultados da pesquisa
            return render(request, 'search_results.html', {'products': products})
    else:
        form = ProductSearchForm()
    
    return render(request, 'search_results.html', {'form': form})