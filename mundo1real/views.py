from itertools import product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from mundo1real.form import ProductSearchForm
from .models import Usuario
from django.contrib.auth import authenticate, login



def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session[ 'usuario']).nome
    return render(request, 'home.html')


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status} )

def cadastro(request):
    status= request.GET.get('status')
    return render (request, 'cadastro.html', {'status': status} )


def cadastrar_usuario(request):
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(email=email)
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect ('/cadastro/?status=1')

        if len(senha) < 8:
            return redirect('/cadastro/?status=2')
        if len(usuario)> 0:
                return redirect ('/cadastro/?status=3')
            
        try:
                usuario = Usuario(email=email, nome=nome, senha=senha)
                usuario.save()

                return redirect('/cadastro/?status=0')
        except:
            return render(request, '/cadastro/?status=4')
    

def fazer_login(request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(email = email).filter(senha = senha)
        
        if len(usuario) == 0:
            return redirect('/login/?status=1')
        elif len(usuario) > 0:
            request.session['usuario'] = usuario[0].id
            return redirect('/home/')
        return HttpResponse(f"{email} {senha}")

def sair(request ):
    request.session.flush()
    return redirect('/login')


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