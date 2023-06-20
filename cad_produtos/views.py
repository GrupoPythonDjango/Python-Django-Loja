from django.shortcuts import render


# Create your views here.
def cadastro_pro(request):
    return render(request, 'cad_produto.html')