from django.shortcuts import render
from .models import Empresa, Tiporisco, Funcao, Descricaoperigo, Inventario
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required        
def home(request):
    empresas = Empresa.objects.all()
    riscos = Tiporisco.objects.all()
    funcao = Funcao.objects.all()
    descricao_perigo = Descricaoperigo.objects.all()
    inventario = Inventario.objects.all()


    return render(request, 'empresa/home.html',
            {
            "empresas": empresas, 
            "riscos": riscos,
            "funcao": funcao,
            "descricao_perigo":descricao_perigo,
            "inventario":inventario,
            }
                )
    
