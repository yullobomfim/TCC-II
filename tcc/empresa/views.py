from django.shortcuts import render
from .models import Empresa, Tiporisco, Funcao, Descricaoperigo

# Create your views here.
def home(request):
    empresas = Empresa.objects.all()
    tipos_risco = Tiporisco.objects.all()
    funcao = Funcao.objects.all()
    descricao_perigo = Descricaoperigo.objects.all()


    return render(request, 'empresa/home.html',
            {
            "empresas": empresas, 
            "tipos_risco": tipos_risco,
            "funcao": funcao,
            "descricao_perigo":descricao_perigo,
            }
                )
